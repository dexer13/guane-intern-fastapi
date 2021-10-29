from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models import User
from app.models.animals import Dog
from app.dependencies import get_current_user
from app.schemas import DogInSchema, DogOutSchema, DogSchema
from app.worker import add_dog

router = APIRouter(
    prefix='/dogs',
    tags=['dogs'],
)


@router.post("/")
async def create_dogs(
        dog: DogInSchema,
        current_user: User = Depends(get_current_user)
):
    add_dog.delay(dog.dict(exclude_unset=True), current_user.id)
    return {'message': 'The dog will be created'}


@router.get("/", response_model=List[DogSchema])
async def get_dogs():
    dogs = await DogSchema.from_queryset(Dog.all())
    return dogs


@router.get("/is_adopted", response_model=List[DogSchema])
async def get_dog():
    return await DogSchema.from_queryset(Dog.filter(is_adopted=True))


@router.get("/{dog_name}")
async def get_dog(dog_name: str):
    return await DogSchema.from_queryset_single(Dog.get(name=dog_name))


@router.delete("/{dog_name}")
async def delete_dog(dog_name: str):
    await Dog.filter(name=dog_name).delete()
    return {'message': f'The dog with name {dog_name} has been deleted'}


@router.put("/{dog_name}", responses={404: {"model": HTTPNotFoundError}})
async def update_dog(dog_name: str, dog: DogInSchema):
    await Dog.filter(name=dog_name).update(**dog.dict(exclude_unset=True))
    return await DogOutSchema.from_queryset_single(Dog.get(name=dog_name))
