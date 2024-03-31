from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Video

def index(request):
    meditations = Video.objects.all()
    template = loader.get_template("mindfulness/index.html")
    context = {
        "meditations": meditations,
    }
    return HttpResponse(template.render(context, request))

