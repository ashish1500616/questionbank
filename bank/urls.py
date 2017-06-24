from django.conf.urls import url
from . import views

app_name = 'bank'

urlpatterns = [
    url(r'^branch/', views.show_branch, name='branch'),
    url(r'^$', views.Frontpage.as_view(), name='front'),

    url(r'^1/$', views.HomeView.as_view(), name='home'),

    url(r'^home2/$', views.Home2View.as_view(), name='home2'),

    url(r'^home1/$', views.Home1View.as_view(), name='home1'),

    url(r'^home3/$', views.Home3View.as_view(), name='home3'),

    url(r'^0/$', views.IndexView.as_view(), name='index'),

    url(r'^2/$', views.Index2View.as_view(), name='index2'),

    url(r'^3/$', views.EceView.as_view(), name='ece'),

    url(r'^4/$', views.Ece2View.as_view(), name='ece2'),

    url(r'^5/$', views.MechView.as_view(), name='mech'),

    url(r'^6/$', views.Mech2View.as_view(), name='mech2'),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),



    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),



    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),


]
