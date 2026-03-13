from redis import Redis
from redis.connection import ConnectionPool


def create_redis_client(redis_url: str) -> Redis:
    pool = ConnectionPool.from_url(redis_url, decode_responses=True)
    return Redis(connection_pool=pool)