from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.url_service import create_short_url, get_original_url

router = APIRouter()

@router.post("/shorten")
async def shorten(url: str):

    code = create_short_url(url)

    return {
        "short_url": f"http://testserver/{code}",
        "original_url": url
    }


@router.get("/{code}")
async def redirect(code: str):

    url = get_original_url(code)

    if not url:
        raise HTTPException(status_code=404)

    return RedirectResponse(url)