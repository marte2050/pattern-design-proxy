import json
import redis.asyncio as redis

class Cache:
    def __init__(self) -> None:
        self.redis_client = redis.Redis(
            host="localhost", 
            port=6379, 
            db=0, 
            decode_responses=True
        )
    
    async def get_cache(self, key: str) -> dict | bool:
        value = await self.redis_client.get(key)
        msg = json.loads(value) if value else False        
        return msg

    async def set_cache(self, key: str, value, expire_seconds: int = 60) -> None:
        await self.redis_client.set(key, json.dumps(value), ex=expire_seconds)