from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wishes$', views.show_wishes),
    url(r'^wishes/new$', views.show_make_wish),
    url(r'^create_wish$', views.create_wish),
    url(r'^delete/(?P<id>\d+)$', views.delete_wish),
    url(r'^wishes/edit/(?P<id>\d+)$', views.show_edit_wish),
    url(r'^grant_wish/(?P<id>\d+)$', views.grant_wish),
    url(r'^update_wish$', views.update_wish),
    url(r'^logout$', views.logout),
    url(r'^wishes/stats$', views.wish_stats),
    url(r'^like_wish/(?P<id>\d+)$', views.like_wish),
    
]