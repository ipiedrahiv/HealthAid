from django.urls import path
from django.urls import path, include
from . import views
from emotiontrack.views import MoodThanks
from django.views.generic import TemplateView

app_name = "emotiontrack"
urlpatterns = [
    path('register_mood/', views.register_mood, name='register_mood'),
    path('thank_you/', MoodThanks.as_view(), name='mood_thanks'),  # Thank you page
]
