""" Music app urls"""
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/714/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    # /music/714/favorite/
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite_view, name='favorite'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
