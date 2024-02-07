from dataclasses import field
import os
from typing import Optional

# One line of FastAPI imports here later 👈
from sqlmodel import Field, SQLModel, Session, create_engine, select


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    alteryx_id: str = field(nullable=True)
    alteryx_api_key: str = field(nullable=True)
    alteryx_api_secret: str = field(nullable=True)