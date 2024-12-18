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

    class SymptomTypes(models.TextChoices):
        HEADACHE = 'headache', 'Head Ache'
        ABDOMINAL_PAIN = 'abdominal-pain', 'Abdominal Pain'
        CHEST_PAIN = 'chest-pain', 'Chest Pain'
        BACK_PAIN = 'back-pain', 'Back Pain'
        SORE_THROAT = 'sore-throat', 'Sore Throat'

    created = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(User, help_text="It is a Foreign key with auth.models.User. Used to manage authentication and accounting.", on_delete=models.CASCADE, default=None)
    
    choice_text = models.CharField('result', max_length=1, choices=SymptomChoices.choices, default=SymptomChoices.NONE)
    
    symptom_type = models.CharField(
        'symptom type', max_length=50, choices=SymptomTypes.choices, default=SymptomTypes.HEADACHE
    )

    #def __str__(self):
    #    return self.choice_text

    def __str__(self):
        return f"{self.get_symptom_type_display()} - {self.get_choice_text_display()}"
