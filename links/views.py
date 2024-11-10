from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from links.forms import LinkForm
from links.models import Link
from links.services import generate_short_url


class LinkListView(ListView):
    """View for displaying a list of all links"""
    model = Link
    paginate_by = 9


class LinkCreateView(CreateView):
    """View for creating a shortened link"""
    model = Link
    form_class = LinkForm
    success_url = reverse_lazy('links:link_list')

    def form_valid(self, form):
        link = form.save(commit=False)
        link.short_url = generate_short_url(link.full_url)
        short_url = f'http://localhost:8000/{link.short_url}'
        messages.success(self.request, f'Shortened link was successfully generated: {short_url}')
        link.save()
        return super().form_valid(form)
