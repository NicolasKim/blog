# -*-coding:utf-8-*-
from rest_framework import viewsets,pagination
from blog.models import Post, Category, Tag
from blog.serializer import BlogSerializer, CategorySerializer, TagSerializer

__author__ = 'jinqiucheng'

class BlogResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100




class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_time')
    serializer_class = BlogSerializer
    pagination_class = BlogResultsSetPagination



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
