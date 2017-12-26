from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    avatar_url = models.URLField(blank=True,null=True);
    user = models.OneToOneField(User,on_delete=models.CASCADE)