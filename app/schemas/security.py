from pydantic import BaseModel
from typing import Text, Optional


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: Optional[str] = None