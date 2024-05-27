from django.urls import path
from django.urls import path, include
from . import views
from emotiontrack.views import MoodThanks
from django.views.generic import TemplateView

app_name = "emotiontrack"
urlpatterns = [
    path('', views.register_mood, name='register_mood'),
    path('mood_dashboard/', views.mood_dashboard, name='mood_dashboard'),
    path('thank_you/', MoodThanks.as_view(), name='mood_thanks'),  # Thank you page
]
