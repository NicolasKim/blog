#-*-coding:utf-8-*-
from rest_framework import viewsets
from django.contrib.auth.models import User
from dreamspace import serializer


__author__ = 'jinqiucheng'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
