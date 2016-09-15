from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # Detail View
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    # /music/714/favorite/
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite_view, name='favorite'),

    # Add View
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # Update view
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # Delete View
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
