from fastapi import Request
from app.shortener import generate_short_code
from app.config import settings

def create_short_url(request: Request, url: str):

    redis = request.app.state.redis

    existing_code = redis.get(f"url:{url}")
    if existing_code:
        return existing_code

    code = generate_short_code()

    redis.set(f"url:{url}", code, ex=settings.SHORT_URL_TTL)
    redis.set(f"code:{code}", url, ex=settings.SHORT_URL_TTL)

    return code


def get_original_url(request: Request, code: str):
    
    return request.app.state.redis.get(f"code:{code}")