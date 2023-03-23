from typing import List
from patrimony_front.controllers.Connection import BackendConnection
from ..models.Liability import LiabilityI

conn = BackendConnection()

async def getOne(id) -> LiabilityI:
    return await conn.get(f"liabilitys/{id}")

async def getAll() -> List[LiabilityI]:
    return await conn.get(f"liabilitys")

async def create(data: LiabilityI) -> LiabilityI:
    return await conn.post("liabilitys", data)

async def update(id, data: LiabilityI) -> LiabilityI:
    return await conn.put(f"liabilitys/{id}", data)

async def deleteAll() -> List[LiabilityI]:
    return await conn.delete("liabilitys")

async def deleteOne(id):
    return await conn.delete(f"liabilitys/{id}")
