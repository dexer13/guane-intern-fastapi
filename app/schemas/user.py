from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import User

UserInSchema = pydantic_model_creator(User, name='UserIn',
                                      exclude_readonly=True)
UserUpdateInSchema = pydantic_model_creator(User, name='UserUpdateIn',
                                            exclude_readonly=True,
                                            exclude=('password', ))
UserOutSchema = pydantic_model_creator(User, name='UserOut',
                                       exclude=('password', ))