from fastapi import FastAPI

from app.config import DataBaseInit


async def init(app: FastAPI):
    await init_db(app)
    load_data()


async def init_db(app: FastAPI):
    db = DataBaseInit.get_instance(app)
    await db.init_database()


def load_data():
    pass