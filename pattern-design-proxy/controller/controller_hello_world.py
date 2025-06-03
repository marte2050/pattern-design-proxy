from proxy import ProxyServiceHelloWorld

class ControllerHelloWorld:
    def __init__(self) -> None:
        self.hello_world_service = ProxyServiceHelloWorld()

    async def get_message(self, id: str) -> dict:
        return await self.hello_world_service.get_message(id)