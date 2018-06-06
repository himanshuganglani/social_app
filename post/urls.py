from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^post/list", views.PostList.as_view(), name='post-list'),
    url(r"^post/add", views.PostCreate.as_view(), name='post-create'),
    url(r"^(?P<pk>[0-9]+)/$", views.PostDetail.as_view(), name='post-detail'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post-delete'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.CommentCreate.as_view(), name='comment-create'),
    # url(r'^post/(?P<pk>[0-9]+)/comment/$', views.commentcreate, name='comment-create'),
    url(r'^post/count/$', views.like_count, name='like-count'),
    url(r'^post/(?P<pk>[0-9]+)/likecount/$', views.like_count, name='like-count'),
    url(r'^post/(?P<pk>[0-9]+)/dislikecount/$', views.dislike_count, name='dislike-count'),
    ]

