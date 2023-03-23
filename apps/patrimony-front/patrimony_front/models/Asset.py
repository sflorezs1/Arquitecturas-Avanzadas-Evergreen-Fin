from typing import List
from pydantic import BaseModel

from patrimony_front.models.Connection import BackendConnection


class AssetI(BaseModel):
    type: str
    value: float
    description: str
    name: str

conn = BackendConnection()

async def getOne(id) -> AssetI:
    return await conn.get(f"assets/{id}")

async def getAll() -> List[AssetI]:
    return await conn.get(f"assets")

async def create(data: AssetI) -> AssetI:
    return await conn.post("assets", data)

async def update(id, data: AssetI) -> AssetI:
    return await conn.put(f"assets/{id}", data)

async def deleteAll() -> List[AssetI]:
    return await conn.delete("assets")

async def deleteOne(id):
    return await conn.delete(f"assets/{id}")
