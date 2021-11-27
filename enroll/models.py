from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     name = models.CharField(max_length=200)
    
class tags(models.Model):
    tag = models.CharField(max_length=30)

class snippet(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField(max_length=50)
    tag = models.ForeignKey(tags,on_delete=models.CASCADE)
