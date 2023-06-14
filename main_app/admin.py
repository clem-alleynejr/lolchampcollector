from django.contrib import admin

from .models import LolChamp, Ability

admin.site.register(LolChamp)
admin.site.register(Ability)
