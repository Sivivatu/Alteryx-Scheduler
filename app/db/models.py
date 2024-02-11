# One line of FastAPI imports here later 👈
from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    email: str
    full_name: str
    disabled: bool = False
    alteryx_id: str | None = None
    alteryx_api_key: str | None = None
    alteryx_api_secret: str | None = None

class UserInDB(Users):
    hashed_password: str

# async def get_username(username: str, session: AsyncSession):