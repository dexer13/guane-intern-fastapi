from tortoise.models import Model
from tortoise import fields


class Dog(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    picture = fields.TextField()
    is_adopted = fields.BooleanField()
    create_date = fields.DatetimeField()

    def __str__(self):
        return self.name

