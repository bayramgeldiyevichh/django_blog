from django.shortcuts import render
from .models import *

def index(request):
    settings = Settings.objects.all()
    about = About.objects.all()
    work = WorkOur.objects.all()
    service = Services.objects.all()
    context = {
        'settings': settings,
        'about': about,
        'work': work,
        'service': service
    }

    return render(request, 'index.html', context)