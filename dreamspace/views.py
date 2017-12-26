#-*-coding:utf-8-*-
from django.http import HttpResponseRedirect

__author__ = 'jinqiucheng'

def index(request):
    return HttpResponseRedirect('/blog/index?page=1')
