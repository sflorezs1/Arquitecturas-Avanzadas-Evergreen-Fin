from enum import Enum

from patrimony_front.models.Connection import BackendConnection


class LiabilityType(Enum):
    LOAN = "Loan"
    TAX = "Tax"

conn = BackendConnection()

async def get_types():
    return await conn.get("liability_types")
