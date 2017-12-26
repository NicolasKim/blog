from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'category',
                    'cover_image',
                    'excerpt',
                    'author',
                    'created_time']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)