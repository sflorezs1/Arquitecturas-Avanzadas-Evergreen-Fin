from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
# Import all models so Tortoise registers them
import patrimony_back.models as models

from patrimony_back.routers.AssetRouter import AssetRouter
from patrimony_back.routers.LiabilityRouter import LiabilityRouter

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://memory:",
    modules={
        "models": [ models ]
    },
    generate_schemas=True,
    add_exception_handlers=True
)

# Add routers
app.include_router(AssetRouter)
app.include_router(LiabilityRouter)