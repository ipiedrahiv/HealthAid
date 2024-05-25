from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import MoodForm
from .models import Choice
"""
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
def index(request):
    if request.method == 'POST':
        selected_mood = request.POST.get('mood')
        new_choice = Choice(owner=request.user, choice_text=selected_mood)
        new_choice.save()
        return redirect('home')  # Redirect to your desired success page
    else:
        choices = Choice.MoodChoices.choices
    return render(request, 'emotiontrack/index.html', {'choices': choices})
"""

class MoodThanks(TemplateView):
    template_name = 'emotiontrack/mood_thanks.html'

mood_thanks = MoodThanks.as_view()

@login_required
def register_mood(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.owner = request.user
            mood.save()
            return redirect('emotiontrack:mood_thanks')  # Redirect to a thank you page or any other page
    else:
        form = MoodForm()
    return render(request, 'emotiontrack/register_mood.html', {'form': form})

