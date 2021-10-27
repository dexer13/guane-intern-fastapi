from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Dog(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, unique=True)
    picture = fields.TextField()
    is_adopted = fields.BooleanField()
    create_date = fields.DatetimeField(auto_now_add=True)
    owner = fields.ForeignKeyField('models.User', related_name='adopted_dogs',
                                   null=True)

    def __str__(self):
        return self.name


