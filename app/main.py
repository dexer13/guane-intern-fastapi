# pylint: disable=E0611,E0401

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.config.parameters import DB_USER, DB_PASS, DB_HOST, DB_PORT, \
    DB_NAME

from app.core.routers import animals, users, files
from app.core.routers import security

ALLOW_ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "https://www.domain.com",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(security.router)
app.include_router(animals.router)
app.include_router(users.router)
app.include_router(files.router)


@app.get("/")
async def root():
    return "Hello denis! I'm working, don't worry."


register_tortoise(
    app,
    db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    modules={'models': ["app.core.models"]},
    add_exception_handlers=True,
    generate_schemas=True
)
# asyncio.create_task(init(app))
