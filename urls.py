from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("mindfulness/", include("mindfulness.urls")),
    path("admin/", admin.site.urls),
]
