from django import forms
from .models import Entry

class EmotionForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['emotion']
