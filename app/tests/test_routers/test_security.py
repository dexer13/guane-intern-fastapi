import pytest
from httpx import AsyncClient

from app.conftest import get_authorization_header
from app.main import app
from app.models import User
from app.utils import Hash


@pytest.mark.asyncio
async def test_get_users():
    data_login = {
        'username': 'user_test',
        'password': 'password_test'
    }
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.post('/login', data=data_login)
        assert response.status_code == 200
        assert response.json().get('access_token', None) is not None
        assert response.json().get('token_type', None) is not None
