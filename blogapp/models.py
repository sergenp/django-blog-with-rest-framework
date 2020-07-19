from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    is_author = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
