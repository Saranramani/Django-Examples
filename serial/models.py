from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=50)

class Track(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='tracks')
    title = models.CharField(max_length=50)
    track = models.CharField(max_length=50)
    duration = models.IntegerField()