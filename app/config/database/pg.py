from app.config.general_config import DB_USER, DB_PASS, DB_HOST, DB_PORT, \
    DB_NAME

TORTOISE_ORM = {
    # "connections": {"default": "mysql://root:123456@127.0.0.1:3306/test"},
    "connections": {"default": f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'},
    "apps": {
        "models": {
            "models": ["app.models.animals", "aerich.models"],
            "default_connection": "default",
        },
    },
}