from tortoise.contrib.pydantic import pydantic_model_creator
from app.core.models import Dog


DogSchema = pydantic_model_creator(Dog, name='Dog',
                                   exclude=('owner.password', ))
DogInSchema = pydantic_model_creator(Dog, name='DogIn', exclude_readonly=True,
                                     exclude=('owner_id',))
DogOutSchema = pydantic_model_creator(
    Dog, name='DogOut', exclude_readonly=True)