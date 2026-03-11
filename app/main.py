from fastapi import FastAPI
from app.routes import urls

app = FastAPI(title="URL Shortener API")

@app.get("/")
async def health_check():
    return {"status": "ok"}

app.include_router(urls.router)
