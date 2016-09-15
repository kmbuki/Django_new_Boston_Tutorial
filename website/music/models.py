from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=200)
    album_logo = models.FileField()


    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk': self.pk})

    def __str__(self):
        return  ' - '.join([self.album_title,  self.artist])

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=300)
    file_type = models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
