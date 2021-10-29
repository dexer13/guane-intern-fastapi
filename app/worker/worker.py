import os
import time
import asyncio
import requests

from celery import Celery
from tortoise import Tortoise

from app.config.general_config import DB_USER, DB_PASS, DB_HOST, DB_PORT, \
    DB_NAME
from app.models import Dog

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


async def init_database():
    await Tortoise.init(
        db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
        modules={'models': ["app.models"]}
    )


@celery.task(name="create_task")
def sleep_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@celery.task(name="add_dog")
def add_dog(dog, user_id):
    requests.post('https://gttb.guane.dev/api/workers?task_complexity=10')
    return asyncio.run(save_dog(dog, user_id))


async def save_dog(dog, user_id):
    await init_database()
    dog_obj = await Dog.create(**dog)
    if dog_obj.is_adopted:
        dog_obj.owner_id = user_id
        await dog_obj.save()
    return True
