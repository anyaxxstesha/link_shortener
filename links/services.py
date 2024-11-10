import random
import string

from links.models import Link


def generate_short_url(full_url):
    """Generates a short URL for the given URL"""
    chars = string.ascii_letters + string.digits
    size = 6
    while True:
        short_url = ''.join(random.choices(chars, k=size))
        if not Link.objects.filter(short_url=short_url).exists():
            break
    return short_url
