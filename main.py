from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, hx_request: Optional[str] = Header(None)):
    films = [
        {'name': 'Blade Runner', 'director': 'Ridley Scott'},
        {'name': 'Pulp Fiction', 'director': 'Quentin Tarantino'},
        {'name': 'Mulholland Drive', 'director': 'David Lynch'},
        {'name': 'The Shawshank Redemption', 'director': 'Frank Darabont'},
    ]
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("partial/table.html", context)

    return templates.TemplateResponse("index.html", context)

