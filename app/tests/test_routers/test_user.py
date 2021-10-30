import pytest
from httpx import AsyncClient

from app.conftest import get_authorization_header
from app.main import app
from app.core.models import User
from app.core.utils import Hash

module_url = '/api/users'

@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(app=app, base_url='http://test') as client:
        headers = await get_authorization_header(client)
        response = await client.get(f'{module_url}/', headers=headers)
        assert response.status_code == 200
        assert len(response.json()) == 3


@pytest.mark.asyncio
async def test_add_user():
    data_user = {
        'username': 'user_to_add', 'password': 'password',
        'email': 'email@email.com', 'name': 'User test to create'
    }
    async with AsyncClient(app=app, base_url='http://test') as client:
        headers = await get_authorization_header(client)
        response = await client.post(
            f'{module_url}/', headers=headers, json=data_user
        )
        assert response.status_code == 200
        assert response.json().get('username') == 'user_to_add'


@pytest.mark.asyncio
async def test_get_current_user():
    async with AsyncClient(app=app, base_url='http://test') as client:
        headers = await get_authorization_header(client)
        response = await client.get(
            f'{module_url}/me', headers=headers
        )
        assert response.status_code == 200
        assert response.json().get('username') == 'user_test'


@pytest.mark.asyncio
async def test_get_user():
    async with AsyncClient(app=app, base_url='http://test') as client:
        headers = await get_authorization_header(client)
        response = await client.get(f'{module_url}/1', headers=headers)
        assert response.status_code == 200
        assert response.json().get('username') == 'user_test'


@pytest.mark.asyncio
async def test_update_user():
    data_updated = {
        'username': 'user_1',
        'email': 'email_changet@email.com', 'name': 'User test to update test'
    }
    async with AsyncClient(app=app, base_url='http://test') as client:
        headers = await get_authorization_header(client)
        response = await client.put(
            f'{module_url}/2', json=data_updated, headers=headers
        )
        assert response.status_code == 200
        user_updated = await User.get(id=2)
        assert user_updated.email == 'email_changet@email.com'


@pytest.mark.asyncio
async def test_delete_user():
    await User.create(
        id=100, username='user_to_remove',
        password=Hash.get_password_hash('password_test'),
        email='email_test2@tests.tests', name='Usuario2')
    async with AsyncClient(app=app, base_url='http://test') as client:
        assert await User.exists(id=100)
        headers = await get_authorization_header(client)
        response = await client.delete(
            f'{module_url}/100', headers=headers
        )
        assert response.status_code == 200
        assert not await User.exists(id=100)
