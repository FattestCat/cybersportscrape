from django.db import models
from datetime import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=datetime.now())
    tags = models.TextField(blank=True)

