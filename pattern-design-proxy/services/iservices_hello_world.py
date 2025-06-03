from abc import ABC, abstractmethod

class IServiceHelloWorld(ABC):
    @abstractmethod
    async def get_message(self, id: str) -> dict: ...