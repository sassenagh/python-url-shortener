import os

class Settings:

    ENV: str = os.getenv("ENV", "dev")

    SHORT_CODE_LENGTH = 6
    SHORT_URL_TTL = 60 * 60 * 24 * 30

    if ENV == "test":
        REDIS_URL = os.getenv(
            "REDIS_URL",
            "redis://redis:6379/0"
        )

    elif ENV == "prod":
        REDIS_URL = os.getenv(
            "REDIS_URL",
            "redis://redis:6379/0"
        )

    else:
        REDIS_URL = os.getenv(
            "REDIS_URL",
            "redis://localhost:6379/0"
        )

settings = Settings()