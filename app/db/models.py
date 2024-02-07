from dataclasses import field
import os
from typing import Optional

# One line of FastAPI imports here later 👈
from sqlmodel import Field, SQLModel, Session, create_engine, select


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    alteryx_id: Optional[str]
    alteryx_api_key: Optional[str]
    alteryx_api_secret: Optional[str]