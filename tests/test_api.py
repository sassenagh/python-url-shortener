import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app


@pytest.mark.asyncio
async def test_health():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_shorten_url():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post("/shorten", params={"url": "https://example.com"})

    assert response.status_code == 200
    data = response.json()

    assert "short_url" in data
    assert "original_url" in data
    assert data["original_url"] == "https://example.com"
    assert data["short_url"].startswith("http://testserver/")
    assert len(data["short_url"].split("/")[-1]) == 6


@pytest.mark.asyncio
async def test_shorten_url_with_long_url():
    long_url = "https://example.com/very/long/path?param1=value1&param2=value2"

    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post("/shorten", params={"url": long_url})

    assert response.status_code == 200
    data = response.json()

    assert data["original_url"] == long_url
    assert data["short_url"].startswith("http://testserver/")