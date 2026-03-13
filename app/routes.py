from fastapi import Request, APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.url_service import create_short_url, get_original_url

router = APIRouter()

@router.post("/shorten")
async def shorten(request: Request, url: str):

    code = create_short_url(request, url)

    return {
        "short_url": f"http://testserver/{code}",
        "original_url": url
    }


@router.get("/{code}")
async def redirect(request: Request, code: str):

    url = get_original_url(request, code)

    if not url:
        raise HTTPException(status_code=404)

    return RedirectResponse(url)