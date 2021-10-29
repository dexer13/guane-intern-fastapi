from app.config.parameters import DB_USER, DB_PASS, DB_HOST, DB_PORT, \
    DB_NAME

TORTOISE_ORM = {
    "connections": {
        "default":
            f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    },
    "apps": {
        "models": {
            "models": ["app.core.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}