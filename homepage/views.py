from django.shortcuts import render

def index(request):
    return render(request, 'homepage/home_dashboard.html')
