from django.urls import path
from django.urls import path, include
from . import views
from symptomtrack.views import SymptomThanks
from django.views.generic import TemplateView

app_name = "symptomtrack"
urlpatterns = [
    path('', views.register_symptom, name='register_symptom'),
    path('symptom_dashboard/', views.symptom_dashboard, name='symptom_dashboard'),
    path('thank_you/', SymptomThanks.as_view(), name='symptom_thanks'),  # Thank you page
]
