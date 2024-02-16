from typing import AsyncGenerator
from dotenv import load_dotenv
import os
from fastapi import Depends

# One line of FastAPI imports here later 👈
# from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from sqlalchemy.orm import sessionmaker

from . import models

# Load environment variables from .env file
load_dotenv() 

# database_url = os.environ.get("DATABASE_URL")
database_url: str= f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine: AsyncEngine = create_async_engine(database_url, echo=True)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def get_user_by_username(username: str, session: AsyncSession = Depends(get_async_session)):
    user = await session.exec(models.User.select().where(models.User.username == username))
    return user