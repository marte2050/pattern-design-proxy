from utils import Cache
from services import IServiceHelloWorld, HelloWorldService

class ProxyServiceHelloWorld(IServiceHelloWorld):

    def __init__(self) -> None:
        self.hello_world_service = HelloWorldService()
        self.cache = Cache()
 
    async def get_message(self, id: str) -> dict:
        cache = await self.cache.get_cache(id)

        if cache:
            return cache
        
        new_mgs = await self.hello_world_service.get_message(id=id)
        await self.cache.set_cache(key=id, value=new_mgs)

        return new_mgs