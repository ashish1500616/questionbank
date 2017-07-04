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

    url(r'^paper/(?P<subid>\d+)/$',
        views.show_paper, name='question_paper'),

    url(r'^paper/(?P<subid>\d+)/approve/$',
        views.comment_approve, name='comment_approve'),
    url(r'^paper/(?P<subid>\d+)/remove/$', views.comment_remove, name='comment_remove'),


]
