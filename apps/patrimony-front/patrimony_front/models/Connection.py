import httpx
import os

from libs.Singleton import Singleton


class BackendConnection(object, metaclass=Singleton):
    """
    Simple httpx client wrapper 
    """
    
    def __init__(self) -> None:
        self.client = httpx.AsyncClient()
        self.base_url = f"{os.getenv('BACKEND_HOST', 'http://0.0.0.0')}:{os.getenv('BACKEND_PORT', '3000')}"
    
    async def get(self, resource):
        return (await self.client.get(f"{self.base_url}/{resource}")).json()
    
    async def post(self, resource, data):
        return (await self.client.post(f"{self.base_url}/{resource}", json=data)).json()
    
    async def put(self, resource, data):
        return (await self.client.put(f"{self.base_url}/{resource}", json=data)).json()

    async def delete(self, resource):
        return (await self.client.delete(f"{self.base_url}/{resource}")).json()