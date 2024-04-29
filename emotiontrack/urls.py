from django.urls import path

from . import views

app_name = "emotiontrack"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:trackable_id>/", views.detail, name="detail"),
    path("<int:trackable_id>/results/", views.results, name="results"),
    path("<int:trackable_id>/vote/", views.vote, name="vote"),
]
