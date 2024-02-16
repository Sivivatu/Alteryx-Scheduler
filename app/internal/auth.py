from datetime import datetime, timedelta
from enum import Enum
import json
from typing import Any
from httpx import get
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.models import CreateUser, TokenData, User, UserInDB
from db.database import get_async_session, get_user_by_username

import logging.config

logger = logging.getLogger(__name__)
log_config_file = "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Tags(Enum):
    auth: str = "auth"
    users: str = "users"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def get_user(username: str, session: AsyncSession = Depends(get_async_session)) -> UserInDB | None:
    if get_user_by_username(username, session) is None:
        return None
    user = get_user_by_username(username, session)
    return UserInDB(**user)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_token = verify_token(token, credentials_exception)
    user = get_user(username=user_token.username)
    if user is None:
        raise credentials_exception

    return user

def verify_token(token: str, credentials_exception):
    try:
        payload: dict[str, Any] = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        # Further validation can be added here (e.g., check if user exists)
        token_data = TokenData(username=username)
        return token_data
    except JWTError:
        raise credentials_exception

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)) -> UserInDB:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def authenticate_user(username: str, password: str, session: AsyncSession = Depends(get_async_session)):
    user = get_user_by_username(username, session)
    logger.info(f"Authenticating User: {user}")
    if not user:
        logger.error(f"User {username} not found")
        return False
    if not verify_password(password, user.hashed_password):
        logger.error(f"User authentication failed for {username}")
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire: datetime = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


router = APIRouter()

@router.post("/token",
              tags=[Tags.auth],
              summary="Generate and access token",)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    """
    Authenticates the user and generates an access token.

    **Args**:
        form_data (OAuth2PasswordRequestForm): The form data containing the username and password.

    **Returns**:
        dict: A dictionary containing the access token and token type.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me",
            response_model=User,
            tags=[Tags.users],
            summary="Get current user")
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
    return current_user

@router.post("/register",
             response_model=CreateUser, 
             tags=["users"],
             summary="Register a new user")
async def register_user(user: CreateUser, session: AsyncSession = Depends(get_async_session)) -> CreateUser:
# Check if username already exists
    async with session as session:
        statement = select(User).where(User.username == user.username)
        result = await session.execute(statement)
        existing_user = result.scalar_one_or_none()
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username already registered"
            )
        # Hash the user's password
        hashed_password: str = hash_password(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user
