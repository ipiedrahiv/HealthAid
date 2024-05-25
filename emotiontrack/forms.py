from django import forms
from django.forms import ModelChoiceField
from .models import Choice

class MoodForm(forms.ModelForm):
    #choice_text = ModelChoiceField(Choice.objects.all(), empty_label=None)
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.RadioSelect
        }
