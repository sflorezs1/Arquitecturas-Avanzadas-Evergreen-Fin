from patrimony_back.models.LiabilityType import LiabilityType
from patrimony_back.models.mixins.AuditMixin import AuditMixin

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Liability(AuditMixin, models.Model):
    """
    Base Liability model
    """

    id = fields.IntField(pk=True, generated=True)
    type = fields.CharEnumField(LiabilityType, null=False)
    value = fields.FloatField(null=False)
    description = fields.TextField(null=True)
    name = fields.CharField(max_length=64)
    

Liability_Pydantic = pydantic_model_creator(Liability, name="Liability")
LiabilityIn_Pydantic = pydantic_model_creator(Liability, name="Liability", exclude_readonly=True)
