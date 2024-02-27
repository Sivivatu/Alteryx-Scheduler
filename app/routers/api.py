import json
import logging
from typing import Optional

from fastapi import APIRouter, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

logger = logging.getLogger(__name__)
log_config_file = (
    "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
)
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

templates = Jinja2Templates(directory="../frontend/templates")


@router.get(
    "/api/toggleSidebar",
    response_class=HTMLResponse,
    tags=["api"],
    include_in_schema=False,
)
async def toggle_sidebar(
    request: Request,
    # token: Annotated[str, Depends(oauth2_scheme)],
    hx_request: Optional[str] = Header(None),
) -> HTMLResponse:
    context = {"request": request}
    if hx_request:
        return templates.TemplateResponse("partials/sidebar-hx.html", context)
