from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.oauthLogin, name='oauthLogin'),
    #url(r'^$', views.oauth, name='oauthToken'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
]
