import asyncio
from datetime import datetime

from fastapi import FastAPI
from app.initializer import init
from app.models.animals import Dog
from app.routers import animals, users, security

app = FastAPI()
app.include_router(security.router)
app.include_router(animals.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {'message': 'Hello denis!!!'}


asyncio.create_task(init(app))
