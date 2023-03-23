from pathlib import Path
from typing_extensions import Annotated
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import patrimony_front.controllers.AssetController as controller
from patrimony_front.models.Asset import AssetI

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=Path(BASE_DIR, "templates/asset"))
assetsRouter = APIRouter(prefix="/assets")

@assetsRouter.get("/create", response_class=HTMLResponse)
async def create_asset(request: Request):
    return templates.TemplateResponse("create.html", {
        "request": request,
        "title": "Registra un nuevo activo",
        "assetTypes": ["Cash",
            "Investment",
            "Property",
            "Equipment"
        ]
    })


@assetsRouter.post("/save")
async def save(request: Request):
    data = await request.form()
    await controller.create({**data})