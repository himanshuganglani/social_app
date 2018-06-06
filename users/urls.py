# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r"^signup", views.signup, name='signup'),
#     ]

from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup/account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r"^profile", views.ProfileList.as_view(), name='profile-list'),
    url(r'^$', views.alt_logout, name='logout-sess'),
    
   
]