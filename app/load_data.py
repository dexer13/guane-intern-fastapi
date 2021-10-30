from tortoise import Tortoise

from app.config.parameters import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from app.core.models import User
from app.core.utils import Hash

from asyncio import run


class LoadDataBase:

    async def load_database(self):
        try:
            await self.init_database()
            await self.load_users()
            return True
        except Exception as e:
            print(e)
            return False

    async def init_database(self):
        await Tortoise.init(
            db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
            modules={'models': ["app.core.models"]}
        )

    async def load_users(self):
        await User.create(
            username='admin', password=Hash.get_password_hash('123'),
            name='Administrador', email='admin@email.com'
        )


if __name__ == '__main__':
    load_db = LoadDataBase()
    result = run(load_db.load_database())
    if result:
        print('SUCCESS')
    else:
        print('ERROR')
