from django.urls import path

from . import views

app_name = "mindfulness"

urlpatterns = [
    path("", views.index, name="mindfulness"),
]
