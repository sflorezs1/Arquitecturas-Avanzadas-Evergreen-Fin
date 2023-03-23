from fastapi import APIRouter
from patrimony_back.models.LiabilityType import LiabilityType


LiabilityTypeRouter = APIRouter(prefix="/liability_types")

@LiabilityTypeRouter.get("")
def get_types():
    return {
        "types": list(LiabilityType)
    }
