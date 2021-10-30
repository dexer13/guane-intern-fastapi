import requests
from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix='/api/files',
    tags=['files'],
)


@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_binary = await file.read()
    res = requests.post(
        'https://gttb.guane.dev/api/files', files={'file': file_binary}
    )
    return res.json()
