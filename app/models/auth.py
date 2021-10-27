from tortoise import Model, fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=100)
    email = fields.CharField(max_length=72)
    name = fields.CharField(max_length=100)

    def __str__(self):
        return self.username






