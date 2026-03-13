from fastapi import FastAPI, HTTPException
from app.config import settings
from app.redis_client import create_redis_client
from app.routes import router
from contextlib import asynccontextmanager
import time

is_ready = False
startup_time = time.time()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global is_ready

    app.state.redis = create_redis_client(settings.REDIS_URL)
    is_ready = True

    yield

    app.state.redis.close()


app = FastAPI(
    title="URL Shortener API",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/ready")
async def readiness_check():
    if not is_ready:
        raise HTTPException(status_code=503, detail="Service not ready")
    return {"status": "ready", "uptime": time.time() - startup_time}


app.include_router(router)