#-*-coding:utf-8-*-
from django.conf.urls import url
from comment import routers
from django.urls import include

__author__ = 'jinqiucheng'

app_name = 'comment'

urlpatterns = [
    url(r'^', include(routers.router.urls)),
]