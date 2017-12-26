#-*-coding:utf-8-*-
from django import forms

from comment.models import Comment

__author__ = 'jinqiucheng'

class CommentForm(forms.ModelForm):
    text = forms.Textarea()
    class Meta:
        model = Comment
        fields = ['text']
