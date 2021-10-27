from abc import ABC, abstractmethod

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from .general_config import IS_TEST, DB_PORT, DB_NAME, DB_USER, \
    DB_PASS, DB_HOST


class DataBaseInit:
    DB_URL = ''
    MODULES = {'models': ["app.models"]}
    GENERATE_SCHEMAS = True
    APP = None

    def __init__(self, app: FastAPI):
        self.APP = app

    async def init_database(self):
        register_tortoise(
            self.APP,
            db_url=self.DB_URL,
            modules=self.MODULES,
            add_exception_handlers=True,
            generate_schemas=True
        )

    @staticmethod
    def get_instance(app: FastAPI):
        if IS_TEST:
            return DBTestInit(app)
        return DBPostgresInit(app)


class DBTestInit(DataBaseInit):
    DB_URL = "sqlite://:memory:"


class DBPostgresInit(DataBaseInit):
    DB_URL = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


Tortoise.init_models(['app.models'], 'models')

