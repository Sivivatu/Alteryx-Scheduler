from modules.schedules import schedules
from fastapi import APIRouter

import logging
import json

router = APIRouter()

logger = logging.getLogger(__name__)
log_config_file = "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}