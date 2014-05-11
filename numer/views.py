from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

from numer.models import Zapis



class ZapisView(generic.ListView):
    template_name = 'numer/zapis_list.html'
    context_object_name = 'latest_zapis_list'
         
    def get_queryset(self):
        """Return the last published number."""
        return Zapis.objects.order_by('-numerek')[:1]

def pobieranienu(request):
    return render(request, 'numer/numer.html')
    
