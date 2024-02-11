from dotenv import load_dotenv
import os

# One line of FastAPI imports here later 👈
# from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from sqlalchemy.orm import sessionmaker

from . import models
# class Hero(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age: Optional[int] = None

# Load environment variables from .env file
load_dotenv() 

# database_url = os.environ.get("DATABASE_URL")
database_url: str= f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine: AsyncEngine = create_async_engine(database_url, echo=True)


async def get_session():
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def get_user_by_username(username: str, session: AsyncSession):
    user = await session.exec(models.Users.select().where(models.Users.username == username))
    return user

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# # Code above omitted 👆

# def create_heroes():
#     hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
#     hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#     hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    
#     print("Before interacting with the database")
#     print("Hero 1:", hero_1)
#     print("Hero 2:", hero_2)
#     print("Hero 3:", hero_3)

#     with Session(engine) as session:
#         session.add(hero_1)
#         session.add(hero_2)
#         session.add(hero_3)

#         session.commit()

# def select_heroes():
#     with Session(engine) as session:
#         statement = select(Hero)
#         heros = session.exec(statement).all()
#         return heros

# def main():
#     create_db_and_tables()
#     create_heroes()
#     select_heroes()

# More code here later 👇

# if __name__ == "__main__":
#     main()