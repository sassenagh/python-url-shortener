from app.redis_client import redis_client
from app.shortener import generate_short_code
from app.config import settings

def create_short_url(url: str):

    existing_code = redis_client.get(f"url:{url}")

    if existing_code:
        return existing_code

    code = generate_short_code()

    redis_client.set(code, url, ex=settings.SHORT_URL_TTL)
    redis_client.set(f"url:{url}", code, ex=settings.SHORT_URL_TTL)

    return code


def get_original_url(code: str):

    return redis_client.get(code)