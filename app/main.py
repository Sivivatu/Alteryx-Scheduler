from typing import Annotated, Optional
from fastapi import Depends, FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer

from database.database import create_db_and_tables, create_heroes, select_heroes

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="templates")

films = [
        {'name': 'Blade Runner', 'director': 'Ridley Scott'},
        {'name': 'Pulp Fiction', 'director': 'Quentin Tarantino'},
        {'name': 'Mulholland Drive', 'director': 'David Lynch'},
        {'name': 'The Shawshank Redemption', 'director': 'Frank Darabont'},
    ]

@app.get("/", response_class=HTMLResponse)
async def root(
                request: Request, 
                hx_request: Optional[str] = Header(None)
            ):
    
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("partial/table.html", context)

    return templates.TemplateResponse("index.html", context)
