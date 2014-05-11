from django.contrib import admin
from pokoje.models import Pokoj
from pokoje.models import Numer

# Register your models here.
class PokojAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Nazwa",               {'fields': ['nazwa']}),
        ("Informacje", {'fields': ['informacje'], 'classes': ['collapse']}),
    ]
admin.site.register(Pokoj, PokojAdmin)

class NumerAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Id Urzytkownika",  {'fields': ['id_user']}),
       ("Id Pokoju",   {'fields': ['id_pokoj']}),
       ("Numerek",   {'fields': ['numerek']}),
    ]
admin.site.register(Numer, NumerAdmin)