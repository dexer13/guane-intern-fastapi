import asyncio

import pytest
from tortoise import Tortoise
from httpx import Headers, AsyncClient

from app.tests.load_data import load_data_test

DB_URL = "sqlite://:memory:"


async def init_db(db_url, create_db: bool = False, schemas: bool = False) -> None:
    """Initial database connection"""
    await Tortoise.init(
        db_url=db_url, modules={"models": ["app.core.models"]},
        _create_db=create_db
    )
    if create_db:
        print(f"Database created! {db_url = }")
    if schemas:
        await Tortoise.generate_schemas()
        print("Success to generate schemas")


async def init(db_url: str = DB_URL):
    await init_db(db_url, True, True)
    await load_data_test()


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await init()
    yield
    await Tortoise._drop_databases()


async def get_authorization_header(client: AsyncClient):
    user_data = {'username': 'user_test', 'password': 'password_test'}
    token = await client.post('/login', data=user_data)
    access_token = token.json().get('access_token')
    headers = Headers({
        'Authorization': f'Bearer {access_token}'
    })
    return headers
