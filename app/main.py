from fastapi import FastAPI, HTTPException
from app.routes import urls
import time

app = FastAPI(title="URL Shortener API")

is_ready = False
startup_time = time.time()

@app.on_event("startup")
async def startup_event():
    global is_ready
    time.sleep(2)
    is_ready = True

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/ready")
async def readiness_check():
    if not is_ready:
        raise HTTPException(status_code=503, detail="Service not ready")
    return {"status": "ready", "uptime": time.time() - startup_time}

app.include_router(urls.router)
