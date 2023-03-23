from pathlib import Path
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from patrimony_front.models.Asset import create
from patrimony_front.models.AssetType import get_types

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=Path(BASE_DIR, "../templates/asset"))
AssetsRouter = APIRouter(prefix="/assets")

@AssetsRouter.get("/create", response_class=HTMLResponse)
async def create_asset(request: Request):
    types = await get_types()
    return templates.TemplateResponse("create.html", {
        "request": request,
        "title": "Registra un nuevo activo",
        "assetTypes": types["types"]
    })

@AssetsRouter.post("/save")
async def save_asset(request: Request):
    data = await request.form()
    return await create({**data})