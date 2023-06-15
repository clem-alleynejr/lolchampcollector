from django.contrib import admin

from .models import LolChamp, Ability, Item

admin.site.register(LolChamp)
admin.site.register(Ability)
admin.site.register(Item)

