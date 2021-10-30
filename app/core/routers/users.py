from typing import List

from fastapi import APIRouter, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.core.dependencies import get_current_user
from app.core.models.auth import User
from app.core.schemas import UserOutSchema, UserInSchema, UserUpdateInSchema
from app.core.utils import Hash

router = APIRouter(
    prefix='/api/users',
    tags=['users'],
    dependencies=[Depends(get_current_user)]
)


@router.post('/', response_model=UserOutSchema)
async def create_user(user: UserInSchema):
    hashed_password = Hash.get_password_hash(user.password)
    user_obj = User(
        username=user.username, password=hashed_password, email=user.email,
        name=user.name
    )
    await user_obj.save()
    return await UserOutSchema.from_tortoise_orm(user_obj)


@router.get('/', response_model=List[UserOutSchema])
async def get_users():
    return await UserOutSchema.from_queryset(User.all())


@router.get('/me')
async def get_current_user(
        current_user: User = Depends(get_current_user)):
    return await UserOutSchema.from_tortoise_orm(current_user)


@router.get('/{user_id}', response_model=UserOutSchema)
async def get_user(user_id: int):
    return await UserOutSchema.from_queryset_single(User.get(id=user_id))


@router.delete('/{user_id}')
async def get_user(user_id: int):
    await User.filter(id=user_id).delete()
    return {'message': f'User with id {user_id} has been deleted'}


@router.put(
    "/{user_id}",
    responses={404: {"model": HTTPNotFoundError}},
    response_model=UserOutSchema
)
async def update_user(user_id: str, user: UserUpdateInSchema):
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await UserOutSchema.from_queryset_single(User.get(id=user_id))
