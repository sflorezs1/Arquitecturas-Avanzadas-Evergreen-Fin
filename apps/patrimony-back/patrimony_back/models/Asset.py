from typing import Any
from patrimony_back.models.AssetType import AssetType
from patrimony_back.models.mixins.AuditMixin import AuditMixin

from pydantic import BaseModel
from tortoise import fields, models


class Asset(AuditMixin, models.Model):
    """
    Base asset model
    """

    id = fields.UUIDField(pk=True)
    type = fields.CharEnumField(AssetType, null=False)
    value = fields.FloatField(null=False)
    description = fields.TextField(null=True)
    name = fields.CharField(max_length=64)
    
class Asset_Pydantic(BaseModel):
    id: Any
    type: AssetType
    value: float
    description: str
    name: str
    created_at: Any

class AssetIn_Pydantic(BaseModel):
    type: AssetType
    value: float
    description: str
    name: str