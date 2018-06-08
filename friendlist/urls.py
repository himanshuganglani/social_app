
from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r"^friend/(?P<pk>[0-9]+)/list", views.FriendList.as_view(), name='friend-list'),
    url(r'^friend/(?P<pk>[0-9]+)/list/$', views.friendlist, name='friend-list'),
    url(r'^friend/request/(?P<pk>[0-9]+)$', views.sendrequest, name='friend-request'),
    ]
    