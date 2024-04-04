from django.db import models

class Entry(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    class Emotion(models.TextChoices):
        HAPPY = 'Happy'
        NORMAL = 'Normal'
        SAD = 'Sad'
    emotion = models.CharField(max_length=20, choices=Emotion.choices, default=Emotion.NORMAL)


