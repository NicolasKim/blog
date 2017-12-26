from django.contrib import admin

# Register your models here.
from userinfo.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['avatar_url']

admin.site.register(UserProfile,UserProfileAdmin)