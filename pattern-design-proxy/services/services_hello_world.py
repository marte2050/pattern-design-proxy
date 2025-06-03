import time
from .iservices_hello_world import IServiceHelloWorld

class HelloWorldService(IServiceHelloWorld):
    async def get_message(self, id: str) -> dict:
        time.sleep(10)
        return {
            "id": id,
            "message": "Hello, World!"
        }