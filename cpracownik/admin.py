from django.contrib import admin
from cpracownik.models import Info

class InfoAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,               {'fields': ['temat']}),
        ("Data", {'fields': ['data']}),
        ("Informacje", {'fields': ['tresc']}),
        ("Pokoj", {'fields': ['p']}),
    ]
    list_display=('temat','data', 'p')
admin.site.register(Info, InfoAdmin)