from fastapi import APIRouter
from controller import ControllerHelloWorld

router_hello_world = APIRouter()

@router_hello_world.get("/{id}",)
async def home(id: str) -> dict:
    controller_hello_world = ControllerHelloWorld()
    msg =  await controller_hello_world.get_message(id = id)
    return msg