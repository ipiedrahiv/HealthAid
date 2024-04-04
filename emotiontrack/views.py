from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmotionForm

from .models import Entry

def index(request):
    emotionForm = EmotionForm()
    return render(request, 'entry/entry.html', {'entry': entry, 'emotionForm': emotionForm})
