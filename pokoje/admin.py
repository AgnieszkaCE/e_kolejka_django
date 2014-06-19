from django.contrib import admin
from pokoje.models import Pokoj
from pokoje.models import Numer

# Register your models here.
class PokojAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,               {'fields': ['nazwa']}),
        ("Informacje", {'fields': ['informacje']}),
    ]
    list_display=('nazwa','informacje')
admin.site.register(Pokoj, PokojAdmin)

class NumerAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,  {'fields': ['id_user']}),
       ("Id Pokoju",   {'fields': ['id_pokoj']}),
       ("Numerek",   {'fields': ['numerek']}),  
    ]
    list_display = ('id_user', 'id_pokoj', 'numerek')
admin.site.register(Numer, NumerAdmin)