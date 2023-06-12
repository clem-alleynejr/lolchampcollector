from django.shortcuts import render

from .models import LolChamp

def home(request):
    return render(request, 'home.html')

def lolchamps_index(request):
    lolchamps = LolChamp.objects.all()
    return render(request, 'lolchamps/index.html', {
        'lolchamps': lolchamps
    })

def about(request):
    return render(request, 'about.html')