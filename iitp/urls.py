from django.conf.urls import url
from . import views

app_name = 'iitp'

urlpatterns = [

    url(r'^$', views.Frontpage.as_view(), name='front'),

    url(r'^stream$', views.Streampage.as_view(), name='stream'),

]