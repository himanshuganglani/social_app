from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^post/list", views.PostList.as_view(), name='post-list'),
    url(r"^post/add", views.PostCreate.as_view(), name='post-create'),
    url(r"^(?P<pk>[0-9]+)/$", views.PostDetail.as_view(), name='post-detail'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post-delete'),
]
