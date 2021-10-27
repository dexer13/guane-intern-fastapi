from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.models import User
from app.utils import Hash, create_access_token

router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user_obj = await User.get(username=request.username)
    if not Hash.verify_password(user_obj.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid password')
    access_token = create_access_token(
        data={"sub": request.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

