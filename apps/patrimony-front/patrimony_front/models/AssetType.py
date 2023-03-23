from enum import Enum

from patrimony_front.models.Connection import BackendConnection


class AssetTypeI(Enum):
    CASH = "Cash"
    INVESTMENT = "Investment"
    PROPERTY = "Property"
    EQUIPMENT = "Equipment"

conn = BackendConnection()

async def get_types():
    return await conn.get("asset_types")
