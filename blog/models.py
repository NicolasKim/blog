import markdown
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    cover_image = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category,related_name='post',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,related_name='post', blank=True)
    author = models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite'])
            self.excerpt = strip_tags(md.convert(self.body))[:200]
        super(Post,self).save(*args,**kwargs)