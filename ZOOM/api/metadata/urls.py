from django.conf.urls import url
from api.metadata.views import (
    FileListView,
    FileDetailView, FileSourceListView, FileSourceDetailView,
    FileUploadView
)

app_name = 'metadata'
urlpatterns = [
    url(r'^upload/$', FileUploadView.as_view(),
        name='file-upload'),
    url(r'^$', FileListView.as_view(), name='file-list'),
    url(r'^sources/$', FileSourceListView.as_view(), name='file-source-list'),
    url(r'^sources/(?P<pk>[^@$&+,/:;=?]+)/', FileSourceDetailView.as_view(),
        name='file-source-detail'),
    url(r'^(?P<pk>[^@$&+,/:;=?]+)/', FileDetailView.as_view(),
        name='file-detail'),
]
