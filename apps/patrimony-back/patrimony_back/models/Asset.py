from patrimony_back.models.AssetType import AssetType

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Asset(models.Model):
    """
    Base asset model
    """

    id = fields.UUIDField(pk=True)
    type = fields.CharEnumField(AssetType, null=False)
    value = fields.FloatField(null=False)
    description = fields.TextField(null=True)
    name = fields.CharField(max_length=64)
    

Asset_Pydantic = pydantic_model_creator(Asset, name="Asset")
AssetIn_Pydantic = pydantic_model_creator(Asset, name="Asset", exclude_readonly=True)