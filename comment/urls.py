#-*-coding:utf-8-*-
from django.conf.urls import url
from django.urls import path
from comment import views

__author__ = 'jinqiucheng'

app_name = 'comment'

urlpatterns = [
    path('post/<int:post_pk>/', views.post_comment, name='post_comment'),
]