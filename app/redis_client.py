from redis import Redis
from redis.connection import ConnectionPool
from app.config import settings

pool = ConnectionPool.from_url(settings.REDIS_URL, decode_responses=True)
redis_client = Redis(connection_pool=pool)