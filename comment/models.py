from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',blank=True,null=True,related_name='child',on_delete=models.CASCADE)
    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-created_time']