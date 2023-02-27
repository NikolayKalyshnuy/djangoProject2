from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=30)
    tag = models.CharField(max_length=30, default='')
    img = models.BinaryField(default=b'')
