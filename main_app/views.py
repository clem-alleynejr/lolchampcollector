from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LolChamp
from .forms import AbilityForm

def home(request):
    return render(request, 'home.html')

def lolchamps_index(request):
    lolchamps = LolChamp.objects.all()
    return render(request, 'lolchamps/index.html', {
        'lolchamps': lolchamps
    })

def about(request):
    return render(request, 'about.html')

def lolchamp_details(request, lolchamp_id):
    lolchamp = LolChamp.objects.get(id=lolchamp_id)
    ability_form = AbilityForm()
    return render(request, 'lolchamps/details.html', {
        'lolchamp': lolchamp,
        'ability_form': ability_form
        })

class LolChampCreate(CreateView):
    model = LolChamp
    fields = '__all__'
    success_url = '/lolchamps/{id}'

class LolChampUpdate(UpdateView):
    model = LolChamp
    fields = ['name', 'role', 'difficulty']

class LolChampDelete(DeleteView):
    model = LolChamp
    success_url = '/lolchamps'

def add_ability(request, lolchamp_id):
    form = AbilityForm(request.POST)
    if form.is_valid():
        new_ability = form.save(commit=False)
        new_ability.lolchamp_id = lolchamp_id
        new_ability.save()
    return redirect('details', lolchamp_id=lolchamp_id)
