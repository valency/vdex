from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Movie(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    t = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag)
