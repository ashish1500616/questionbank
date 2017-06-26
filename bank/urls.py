from django.conf.urls import url
from . import views

app_name = 'bank'
#[-BIT]IT\W\d+\W+
urlpatterns = [
    url(r'^$', views.indexPage, name='indexpage'),

    url(r'^college/(?P<pk>\d+)/$', views.show_branch, name='branch'),

    url(r'^college/(?P<cid>\d+)/branch/(?P<bid>\d+)/semester/(?P<sid>\d+)/$',
        views.show_subject, name='subject'),

    url(r'^college/(?P<cid>\d+)/branch/(?P<bbid>\d+)/$',
        views.show_sem, name="semester"),

    url(r'^college/(?P<cid>\d+)/branch/(?P<bid>\d+)/semester/(?P<semid>\d+)/paper/(?P<subid>\d+)/$',
        views.show_paper, name='question_paper'),




]
