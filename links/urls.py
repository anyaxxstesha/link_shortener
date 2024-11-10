from django.urls import path

from links.apps import LinksConfig
from links.views import LinkListView

app_name = LinksConfig.name

urlpatterns = [
    path('', LinkListView.as_view(), name='link_list'),
]
