from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    blogpost = models.CharField(max_length=1000)
    created=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User)
    id=models.AutoField(primary_key=True)
    def __unicode__(self):
        return self.title