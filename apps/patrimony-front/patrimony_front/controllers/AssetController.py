from typing import List
from patrimony_front.controllers.Connection import BackendConnection
from ..models.Asset import AssetI

conn = BackendConnection()

async def getOne(id) -> AssetI:
    return await conn.get(f"assets/{id}")

async def getAll() -> List[AssetI]:
    return await conn.get(f"assets")

async def create(data: AssetI) -> AssetI:
    print(data)
    return await conn.post("assets", data)

async def update(id, data: AssetI) -> AssetI:
    return await conn.put(f"assets/{id}", data)

async def deleteAll() -> List[AssetI]:
    return await conn.delete("assets")

async def deleteOne(id):
    return await conn.delete(f"assets/{id}")
