#-*-coding:utf-8-*-
__author__ = 'jinqiucheng'
from comment.models import Comment
from django import template

register = template.Library()
@register.simple_tag()
def get_comments(post):
    return Comment.objects.all().filter(post=post).order_by('-created_time')