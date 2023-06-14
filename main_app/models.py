from django.db import models
from django.urls import reverse

class LolChamp(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'lolchamp_id': self.id})
    
class Ability(models.Model):
    name = models.CharField('ability name', max_length=100)
    description = models.CharField(max_length=500)

    lolchamp = models.ForeignKey(LolChamp, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ability: {self.name} -- Description: {self.description}'
    

                      


