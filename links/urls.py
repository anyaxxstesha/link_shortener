from django.urls import path

from links.apps import LinksConfig
from links.views import LinkListView, LinkCreateView

app_name = LinksConfig.name

urlpatterns = [
    path('', LinkListView.as_view(), name='link_list'),
    path('create/', LinkCreateView.as_view(), name='link_create')
]
