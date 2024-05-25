import django
from django.db import models
from django.contrib.auth.models import  User, Group

"""
class Trackable(models.Model):
    trackable_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.trackable_text
"""

class Choice(models.Model):
    
    class MoodChoices(models.TextChoices):
        AWFUL = '0', 'Awful'
        BAD = '1', 'Bad'
        MEH = '2', 'Meh'
        GOOD = '3', 'Good'
        GREAT = '4', 'Great'

    owner = models.ForeignKey(User, help_text="It is a Foreign key with auth.models.User. Used to manage authentication and accounting.", on_delete=models.CASCADE, default=None)
    choice_text = models.CharField('result', max_length=1, choices=MoodChoices.choices, default=MoodChoices.GOOD)
    def __str__(self):
        return self.choice_text

