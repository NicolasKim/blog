#-*-coding:utf-8-*-
from django import template

from blog.models import Post, Category, Tag

__author__ = 'jinqiucheng'



register = template.Library()

@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag()
def get_categorys():
    return Category.objects.all()

@register.simple_tag()
def get_tags():
    return Tag.objects.all()


