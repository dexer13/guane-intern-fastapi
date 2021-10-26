import asyncio
from datetime import datetime

from fastapi import FastAPI
from app.initializer import init
from app.models.animals import Dog

app = FastAPI()


@app.get("/")
async def root():
    dog = Dog(name='Lucky', picture='', is_adopted=False,
              create_date=datetime.now())
    await dog.save()
    return {'message': 'Hello denis!!!'}


asyncio.create_task(init(app))
