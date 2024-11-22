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
    
    class SymptomChoices(models.TextChoices):
        EXTREME = '0', 'Extreme'
        SEVERE = '1', 'Severe'
        MODERATE = '2', 'Moderate'
        MILD = '3', 'Mild'
        NONE = '4', 'None'

    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, help_text="It is a Foreign key with auth.models.User. Used to manage authentication and accounting.", on_delete=models.CASCADE, default=None)
    choice_text = models.CharField('result', max_length=1, choices=SymptomChoices.choices, default=SymptomChoices.NONE)
    def __str__(self):
        return self.choice_text
