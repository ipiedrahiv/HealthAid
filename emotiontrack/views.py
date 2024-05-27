from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.db.models import Count
import plotly.graph_objs as go
import plotly.offline as opy
import plotly.express as px
from plotly.subplots import make_subplots
from django.utils import timezone
from datetime import timedelta

from .forms import MoodForm
from .models import Choice

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
            return redirect('emotiontrack:mood_dashboard')  # Redirect to a thank you page or any other page
    else:
        form = MoodForm()
    return render(request, 'emotiontrack/register_mood.html', {'form': form})

@login_required
def mood_dashboard(request):
    # Get the current date and time
    now = timezone.now()
    # Calculate the date for one month ago
    one_month_ago = now - timedelta(days=30)

    moods = Choice.objects.filter(owner=request.user, created__gte=one_month_ago)
    mood_counts = moods.values('choice_text').annotate(count=Count('choice_text'))

    total_choices = len(Choice.MoodChoices.choices)
    y = [0] * total_choices
    
    # Fill the list with counts from the queryset
    for mood_count in mood_counts:
        index = int(mood_count['choice_text'])  # Convert choice_text to an index
        y[index] = mood_count['count']


    print(y)

    x = ["Awful", "Bad", "Meh", "Good", "Great"]

    line_x = [mood.created for mood in moods]
    line_y = [mood.get_choice_text_display() for mood in moods]

    return render(
            request,
            'emotiontrack/mood_dashboard.html',
            {
                "spider_graph": create_spider_graph(x, y),
                "line_graph": create_line_graph(line_x, line_y),
            },
        )

def create_spider_graph(x, y):
    fig = go.Figure(data=go.Scatterpolar(
        r=y,
        theta=x,
        fill='toself'
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            ),
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False
    )
    div = opy.plot(fig, auto_open=False, output_type="div")
    return div

def create_line_graph(x, y):
    mood_mapping = {"Awful": 0, "Bad": 1, "Meh": 2, "Good": 3, "Great": 4}
    y = [mood_mapping[mood] for mood in y]
    
    data = [go.Scatter(x=x, y=y)]
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis={"title": "Date"},
        yaxis={
            "title": "Mood",
            "range": [0, 4],
            "tickvals": [0, 1, 2, 3, 4],
            "ticktext": ["Awful", "Bad", "Meh", "Good", "Great"]
        },
        margin=dict(l=20, r=20, t=20, b=20),
    )
    fig = go.Figure(data=data, layout=layout)
    div = opy.plot(fig, auto_open=False, output_type="div")
    return div
