from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from app.core.models import User
from app.core.utils import Hash, create_access_token

from celery.result import AsyncResult
from app.worker import sleep_task

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


@router.get('/sleep/{time}')
async def sleep_by_time(time):
    task = sleep_task.delay(time)
    return JSONResponse({'task_id': task.id})


@router.get("/tasks/{task_id}")
def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)

