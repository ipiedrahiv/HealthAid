from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

from .models import Trackable, Choice

def index(request):
    latest_question_list = Trackable.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "emotiontrack/index.html", context)

def detail(request, trackable_id):
    trackable = get_object_or_404(Trackable, pk=trackable_id)
    return render(request, "emotiontrack/detail.html", {"trackable": trackable})

def results(request, trackable_id):
    response = "You have checked in!"
    return HttpResponse(response)

def vote(request, trackable_id):
    trackable = get_object_or_404(Trackable, pk=trackable_id)
    try:
        selected_choice = trackable.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "emotiontrack/detail.html",
            {
                "trackable": trackable,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("emotiontrack:results", args=(trackable.id,)))
