from django.urls import path

from links.apps import LinksConfig
from links.views import LinkListView, LinkCreateView, LinkRedirectView

app_name = LinksConfig.name

urlpatterns = [
    path('links', LinkListView.as_view(), name='link_list'),
    path('links/create', LinkCreateView.as_view(), name='link_create'),
    path('<str:short_url>', LinkRedirectView.as_view(), name='link_redirect'),
]
