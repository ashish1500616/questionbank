from django.conf.urls import url
from . import views

app_name = 'bank'

urlpatterns = [
    url(r'^home/$', views.HomeView.as_view(), name='home'),

    url(r'^home2/$', views.Home2View.as_view(), name='home2'),


    url(r'^$', views.IndexView.as_view(), name='index'),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),



    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),



    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),


]
