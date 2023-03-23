from pydantic import BaseModel
from .LiabilityType import LiabilityTypeI


class LiabilityI(BaseModel):
    type: str
    value: float
    description: str
    name: str