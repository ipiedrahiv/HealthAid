from django.contrib import admin

# Register your models here.
from .models import Choice

"""admin.site.register(Trackable)"""
admin.site.register(Choice)
