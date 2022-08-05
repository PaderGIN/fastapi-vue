import os


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}