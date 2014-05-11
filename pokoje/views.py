
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context import Context, RequestContext
from django.views import generic
from django.shortcuts import get_object_or_404

from pokoje.models import Numer
from pokoje.models import Pokoj
from django.contrib.auth.models import User

def numerek(self):
    ostatni = Numer.objects.order_by('-id')[0] 
    return HttpResponse("Numer: %s" % ostatni.numerek)
# Create your views here.
class PokojView(generic.ListView):
    # View code here...
    template_name = '/pokoje/pokoje.html'
    context_object_name = 'latest_pokoje_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Pokoj.objects.order_by('-nazwa')[:5]
    
    #def numerek(self):
    #    return Numer.objects.order_by('-id')[0] 
    #return HttpResponse("Numer: %s" % ostatni.numerek)

class DetailView(generic.ListView):
    model = Numer
    template_name = 'pokoje/detail.html'
    context_object_name = 'latest_numer_list'
    
    def get_queryset(self):
        """Return the last five published polls."""
        return Numer.objects.order_by('-numerek')[:1]
  
def vote(request, pokoj_id):
    
    p = get_object_or_404(Pokoj, pk=pokoj_id)
     
    
    


    