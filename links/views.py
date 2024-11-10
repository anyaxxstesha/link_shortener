from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, RedirectView

from links.forms import LinkForm
from links.models import Link
from links.services import generate_short_url, get_full_url


class LinkListView(ListView):
    """View for displaying a list of all links"""
    model = Link
    paginate_by = 9

    def paginate_queryset(self, queryset, page_size):
        paginator, page_obj, object_list, has_other_pages = super().paginate_queryset(queryset, page_size)
        for obj in object_list:
            obj.short_url = f"{settings.SCHEME}://{settings.DOMAIN}:{settings.PORT}/{obj.short_url}"
        return paginator, page_obj, object_list, has_other_pages



class LinkCreateView(CreateView):
    """View for creating a shortened link"""
    model = Link
    form_class = LinkForm
    success_url = reverse_lazy('links:link_list')

    def form_valid(self, form):
        link = form.save(commit=False)
        link.short_url = generate_short_url()
        short_url = f'{settings.SCHEME}://{settings.DOMAIN}:{settings.PORT}/{link.short_url}'
        messages.success(self.request, f'Shortened link was successfully generated: {short_url}')
        link.save()
        return super().form_valid(form)


class LinkRedirectView(RedirectView):
    """Redirect view for shortened links"""

    def get_redirect_url(self, *args, **kwargs):
        return get_full_url(self.kwargs.get('short_url', ''))
