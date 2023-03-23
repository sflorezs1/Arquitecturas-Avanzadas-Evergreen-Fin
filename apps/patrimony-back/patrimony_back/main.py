from fastapi import FastAPI
from patrimony_back.routers.LiabilityTypeRouter import LiabilityTypeRouter
from patrimony_back.routers.AssetTypeRouter import AssetTypeRouter
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
app.include_router(AssetTypeRouter)
app.include_router(LiabilityTypeRouter)