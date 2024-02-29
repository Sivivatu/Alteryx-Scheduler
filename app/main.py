import json

# from app.routers import alt_schedules
import logging.config
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from app.db.models import Users
from internal import auth
from internal.auth import oauth2_scheme
from routers import api

logger = logging.getLogger(__name__)
log_config_file = (
    "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
)
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

logger.info("Starting FastAPI app")
app = FastAPI()
# app.include_router(alt_schedules.router)
app.include_router(auth.router)
app.include_router(api.router)

logger.info("Adding CORS middleware")
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/images", StaticFiles(directory="../frontend_hx/templates/images"), name="images"
)
app.mount(
    "/partials",
    StaticFiles(directory="../frontend_hx/templates/partials"),
    name="partials",
)
app.mount("/css", StaticFiles(directory="../frontend_hx/templates/css"), name="css")
app.mount("/js", StaticFiles(directory="../frontend_hx/templates/js"), name="js")
app.mount(
    "/fonts", StaticFiles(directory="../frontend_hx/templates/fonts"), name="fonts"
)
app.mount(
    "/favicon.ico",
    StaticFiles(directory="../frontend_hx/templates"),
    name="favicon.ico",
)

templates = Jinja2Templates(directory="../frontend_hx/templates")

films = [
    {"name": "Blade Runner", "director": "Ridley Scott"},
    {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
    {"name": "Mulholland Drive", "director": "David Lynch"},
    {"name": "The Shawshank Redemption", "director": "Frank Darabont"},
]


@app.get("/index", response_class=HTMLResponse)
async def read_index(request: Request, response_class=HTMLResponse):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)
    # return {token: token}


@app.get("/")
async def read_root(request: Request):
    return {"message": "Hello World"}


# @app.get("/admin")
# async def admin_tests(request: Request, response_class=HTMLResponse):
#     context = {"request": request}
#     return templates.TemplateResponse("index-admin.html", context)
#     # return {token: token}


@app.get("/movies", response_class=HTMLResponse)
async def root(
    request: Request,
    # token: Annotated[str, Depends(oauth2_scheme)],
    hx_request: Optional[str] = Header(None),
) -> HTMLResponse:
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("partial/table.html", context)

    return templates.TemplateResponse("index-hx.html", context)
