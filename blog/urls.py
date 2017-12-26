#-*-coding:utf-8-*-
from django.conf.urls import url
from django.urls import path

from blog import views

__author__ = 'jinqiucheng'

app_name = 'blog'

urlpatterns = [
    url(r'^index$', views.BlogList.as_view(),name='blog-index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.BlogDetail.as_view(), name='blog-detail'),
    path('category/<int:pk>/', views.CategoryList.as_view(), name='category-list'),
    path('tag/<int:pk>/', views.TagList.as_view(), name='tag-list'),
]

