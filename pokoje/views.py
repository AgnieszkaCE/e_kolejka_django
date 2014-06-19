
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from pokoje.models import Numer
from pokoje.models import Pokoj


def numerek(self):
    ostatni = Numer.objects.order_by('-id')[0] 
    return HttpResponse("Numer: %s" % ostatni.numerek)

def ostatni(request, pk):
    q = Numer.objects.filter(id_pokoj = pk).order_by('-id').values()[:1]
    #q = q.extra(order_by = ['-numerek'][:0])
    tmp = q[0]['numerek']
    return HttpResponse("Numerek: %s" % tmp)
    #return Numer.objects.filter(id_pokoj = pk).order_by('-numerek')[:1]
# Create your views here.
class PokojView(generic.ListView):
    # View code here...
    template_name = '/pokoje/pokoje.html'
    context_object_name = 'latest_pokoje_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Pokoj.objects.order_by('-nazwa')
    

class NumerView(generic.ListView):
    model = Numer
    template_name = 'pokoje/detail.html'
    context_object_name = 'latest_numer_list'
    
    def get_queryset(self):
        """Return the last five published polls."""
        pk = self.kwargs['pk']
        #return Numer.objects.order_by('-numerek')[:1]
        return Numer.objects.filter(id_pokoj = pk).order_by('-numerek')[:1]
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NumerView, self).get_context_data(**kwargs)
        # Add something
        pk = self.kwargs['pk']
        zmienna = Pokoj.objects.filter(id = pk)[0]
        context['nazwa_pokoju'] = zmienna.nazwa
        return context
  
        
                         
  
def vote(self, pk):

    tmp = Pokoj.objects.get(id = pk)
    osoba = self.user
    czlowiek = get_object_or_404(User, id = osoba.id)
    numerr = Numer.objects.filter(id_pokoj = pk).order_by('-id').values()[:1]
      
    Numer.objects.create(id_pokoj = tmp, id_user = czlowiek, numerek = numerr[0]['numerek'] + 1)
    #p.id_pokoj = tmp 
    #p.id_user = czlowiek
    #p.numerek = 4
    #p.save
    return HttpResponseRedirect("/") 
    


    