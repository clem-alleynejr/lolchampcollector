from django.shortcuts import render

lolchamps = [
    {'name': 'Ekko', 'role': 'Assassin', 'difficulty': 'High'},
    {'name': 'Miss Fortune', 'role': 'Marksman', 'difficulty': 'Low'}
]

def home(request):
    return render(request, 'home.html')

def lolchamps_index(request):
    return render(request, 'lolchamps/index.html', {
        'lolchamps': lolchamps
    })

def about(request):
    return render(request, 'about.html')