from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .views.AssetView import assetsRouter

app = FastAPI()
import os
BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=Path(BASE_DIR, "static")), name="static")

app.include_router(assetsRouter)