from datetime import timedelta, datetime

from fastapi import HTTPException
from jose import jwt, JWTError

from app.schemas import TokenDataSchema

SECRET_KEY = '3e7fd6140e32b756a495477dc529d85f3d9dab279f1de04ae8884f1e7bd38d9c'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenDataSchema(username=username)
        return token_data
    except JWTError:
        raise credentials_exception
