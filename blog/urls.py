#-*-coding:utf-8-*-
from django.conf.urls import url
from blog import routers
from django.urls import include

__author__ = 'jinqiucheng'

app_name = 'blog'
urlpatterns = [
    url(r'^', include(routers.router.urls)),
]

