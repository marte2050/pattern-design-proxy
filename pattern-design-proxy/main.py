from fastapi import FastAPI
from router import router_hello_world

app = FastAPI()

app.include_router(router_hello_world)