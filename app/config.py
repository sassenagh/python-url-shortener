import os

class Settings:

    ENV: str = os.getenv("ENV", "dev")

    if ENV == "test":
        DATABASE_URL = "sqlite:///:memory:"
        REDIS_URL = "redis://localhost:6379/1"

    elif ENV == "prod":
        DATABASE_URL = os.getenv(
            "DATABASE_URL",
            "postgresql://app:app@db:5432/app"
        )
        REDIS_URL = os.getenv(
            "REDIS_URL",
            "redis://redis:6379/0"
        )

    else:  # dev
        DATABASE_URL = "postgresql://app:app@db:5432/app"
        REDIS_URL = "redis://redis:6379/0"


settings = Settings()