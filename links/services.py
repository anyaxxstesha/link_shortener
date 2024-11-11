import random
import string

from django.http import Http404

from links.models import Link


def generate_short_url():
    """Generates a short URL"""
    chars = string.ascii_letters + string.digits
    size = 6
    while True:
        short_url = ''.join(random.choices(chars, k=size))
        if not Link.objects.filter(short_url=short_url).exists():
            break
    return short_url

def get_full_url(shortened_url):
    """Retrieves the full URL associated with the given short URL"""
    try:
        link = Link.objects.get(short_url=shortened_url)
    except Link.DoesNotExist:
        return None
    return link.full_url
