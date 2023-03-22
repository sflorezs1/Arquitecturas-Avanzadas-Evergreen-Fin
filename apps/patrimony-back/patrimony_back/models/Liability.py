from typing import Any
from patrimony_back.models.LiabilityType import LiabilityType
from patrimony_back.models.mixins.AuditMixin import AuditMixin
from pydantic import BaseModel

from tortoise import fields, models


class Liability(AuditMixin, models.Model):
    """
    Base Liability model
    """

    id = fields.IntField(pk=True, generated=True)
    type = fields.CharEnumField(LiabilityType, null=False)
    value = fields.FloatField(null=False)
    description = fields.TextField(null=True)
    name = fields.CharField(max_length=64)
    

class Liability_Pydantic(BaseModel):
    id: Any
    type: LiabilityType
    value: float
    description: str
    name: str
    created_at: Any


class LiabilityIn_Pydantic(BaseModel):
    type: LiabilityType
    value: float
    description: str
    name: str