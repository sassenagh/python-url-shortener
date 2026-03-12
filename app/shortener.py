import random
import string
from app.config import settings

ALPHABET = string.ascii_letters + string.digits

def generate_short_code():
    return "".join(
        random.choice(ALPHABET)
        for _ in range(settings.SHORT_CODE_LENGTH)
    )