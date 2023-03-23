from pathlib import Path
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from patrimony_front.models.Liability import create
from patrimony_front.models.LiabilityType import get_types

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=Path(BASE_DIR, "../templates/liability"))
LiabilitysRouter = APIRouter(prefix="/liabilitys")

@LiabilitysRouter.get("/create", response_class=HTMLResponse)
async def create_liability(request: Request):
    types = await get_types()
    return templates.TemplateResponse("create.html", {
        "request": request,
        "title": "Registra un nuevo pasivo",
        "liabilityTypes": types["types"]
    })

@LiabilitysRouter.post("/save")
async def save_liability(request: Request):
    data = await request.form()
    return await create({**data})