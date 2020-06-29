from django.db import models
import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())  # add now time if datetime isn't specified