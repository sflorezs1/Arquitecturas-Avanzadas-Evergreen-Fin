from pydantic import BaseModel
from .AssetType import AssetTypeI


class AssetI(BaseModel):
    type: str
    value: float
    description: str
    name: str