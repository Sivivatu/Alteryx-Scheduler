# One line of FastAPI imports here later 👈
from sqlmodel import Field, SQLModel

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: str | None = None

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    # email: str
    # full_name: str
    disabled: bool = False
    # alteryx_id: str | None = None
    # alteryx_api_key: str | None = None
    # alteryx_api_secret: str | None = None

class UserInDB(User):
    hashed_password: str
    disabled: bool

class CreateUser(User):
    username: str = Field(index=True, unique=True)
    password: str

class UserUpdate(User):
    username: str
    email: str
    full_name: str
    disabled: bool
    alteryx_id: str
    alteryx_api_key: str
    alteryx_api_secret: str