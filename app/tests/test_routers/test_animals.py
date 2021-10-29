import pytest
from httpx import AsyncClient

from app.conftest import get_authorization_header
from app.main import app
from app.models import Dog


@pytest.mark.asyncio
async def test_get_dogs():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get('/dogs/', headers={})
        assert response.status_code == 200
        assert len(response.json()) == 3


@pytest.mark.asyncio
async def test_add_dog_unauthorized():
    dog_data = {'name': 'lucky', 'picture': 'lucky.png', 'is_adopted': True}
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post('/dogs/', json=dog_data)
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_add_dog():
    dog_data = {'name': 'lucky', 'picture': 'lucky.png', 'is_adopted': True}
    async with AsyncClient(app=app, base_url="http://test") as client:
        headers = await get_authorization_header(client)
        response = await client.post(
            '/dogs/', json=dog_data,
            headers=headers
        )
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_dog():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get('/dogs/lucky')
        assert response.status_code == 200
        assert response.json().get('name') == 'lucky'


@pytest.mark.asyncio
async def test_get_adopted_dogs():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get('/dogs/is_adopted')
        assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_update_dog():
    data_updated = {'name': 'penelope', 'picture': 'penelope.png',
                    'is_adopted': True}
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.put('/dogs/penelope', json=data_updated)
        assert response.status_code == 200
        dog_obj_updated = await Dog.get(name='penelope')
        assert dog_obj_updated.picture == 'penelope.png'


@pytest.mark.asyncio
async def test_delete_dog():
    await Dog.create(name='dog_to_deleted', picture='default.png',
                     is_adopted=False)
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.delete('/dogs/dog_to_deleted')
        assert response.status_code == 200
        assert not await Dog.exists(name='dog_to_deleted')


