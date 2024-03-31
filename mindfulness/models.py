from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = EmbedVideoField()
