from fastapi import APIRouter, Request
import random
import string

router = APIRouter()

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@router.post("/shorten")
async def shorten_url(url: str, request: Request):
    code = generate_code()
    base_url = str(request.base_url).rstrip('/')
    return {
        "short_url": f"{base_url}/{code}",
        "original_url": url
    }