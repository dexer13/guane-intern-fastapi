from app.core.models import User, Dog
from app.core.utils import Hash


async def load_data_test():
    await load_data_animals()
    await load_data_users()


async def load_data_animals():
    await Dog.create(name='lucky', picture='default.png', is_adopted=True)
    await Dog.create(name='luna', picture='default.png', is_adopted=False)
    await Dog.create(name='penelope', picture='default.png', is_adopted=False)


async def load_data_users():
    await User.create(id=1, username='user_test',
                      password=Hash.get_password_hash('password_test'),
                      email='email_test@tests.tests', name='Usuario')
    await User.create(id=2, username='user_1',
                      password=Hash.get_password_hash('password_test'),
                      email='email_test1@tests.tests', name='Usuario1')
    await User.create(username='user_2',
                      password=Hash.get_password_hash('password_test'),
                      email='email_test2@tests.tests', name='Usuario2')