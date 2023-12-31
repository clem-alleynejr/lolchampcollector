from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import LolChamp, Item
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
    id_list = lolchamp.items.all().values_list('id')
    items_lolchamp_doesnt_have = Item.objects.exclude(id__in=id_list)
    ability_form = AbilityForm()
    return render(request, 'lolchamps/details.html', {
        'lolchamp': lolchamp,
        'ability_form': ability_form,
        'items': items_lolchamp_doesnt_have
        })

def assoc_item(request, lolchamp_id, item_id):
   LolChamp.objects.get(id=lolchamp_id).items.add(item_id)
   return redirect ('details', lolchamp_id=lolchamp_id)

class LolChampCreate(CreateView):
    model = LolChamp
    fields = ['name', 'role', 'difficulty']
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

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'description', 'cost']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items'
