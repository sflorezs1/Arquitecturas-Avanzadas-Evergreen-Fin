
from fastapi import APIRouter
from patrimony_back.models.AssetType import AssetType


AssetTypeRouter = APIRouter(prefix="/asset_types")

@AssetTypeRouter.get("")
def get_types():
    return {
        "types": list(AssetType)
    }
