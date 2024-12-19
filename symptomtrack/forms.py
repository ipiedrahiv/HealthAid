from django import forms
from django.forms import ModelChoiceField
from .models import Choice

#class SymptomForm(forms.ModelForm):
#    #choice_text = ModelChoiceField(Choice.objects.all(), empty_label=None)
#    class Meta:
#        model = Choice
#        fields = ['choice_text']
#        widgets = {
#            'choice_text': forms.RadioSelect
#        }

class SymptomForm(forms.ModelForm):
    choice_text = forms.ChoiceField(
        choices=Choice.SymptomChoices.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    symptom_type = forms.ChoiceField(
        choices=Choice.SymptomTypes.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Choice
        fields = ['choice_text', 'symptom_type']
