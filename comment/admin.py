from django.contrib import admin

# Register your models here.
from comment.models import Comment
#
# class CommentAdmin(admin.ModelAdmin):
#     fields = ['text']
#

admin.site.register(Comment)