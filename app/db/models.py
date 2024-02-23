# One line of FastAPI imports here later 👈
from sqlmodel import Field, SQLModel

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: str | None = None

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    disabled: bool = False

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    hashed_password: str
    email: str | None = Field(default=None, index=True)
    full_name: str | None = Field(default=None)
    alteryx_id: str | None = Field(default=None)
    alteryx_api_key: str | None = Field(default=None)
    alteryx_api_secret: str | None = Field(default=None)


class UserInDB(UserBase):
    pass

class CreateUser(UserBase):
    password: str
    email: str | None = Field(default=None, index=True)

class ReadCreatedUser(UserBase):
    id: int
    username: str
    email: str | None

class ReadUser(UserBase):
    id: int
    username: str
    email: str
    full_name: str
    disabled: bool
    alteryx_id: str
    alteryx_api_key: str
    alteryx_api_secret: str

class UserUpdate(UserBase):
    username: str
    email: str
    full_name: str
    disabled: bool
    alteryx_id: str
    alteryx_api_key: str
    alteryx_api_secret: str