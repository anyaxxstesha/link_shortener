from django.views.generic import ListView

from links.models import Link


class LinkListView(ListView):
    """View for displaying a list of all links"""
    model = Link
    paginate_by = 20
