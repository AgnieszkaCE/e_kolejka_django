from audioop import reverse
from django.contrib.auth.models import User, Group
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render
from django.template.context import RequestContext
from django.views import generic

from cpracownik.models import Info
from pokoje.models import Numer
from pokoje.models import Pokoj


class Index(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'info_list'

    def get_queryset(self):
        return Info.objects.order_by('-data')[:5]



class PokojView(generic.ListView):
    # View code here...
    template_name = 'pokoje/pokoje.html'
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
        return Numer.objects.filter(id_pokoj = pk).order_by('numerek')[:1]
  
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NumerView, self).get_context_data(**kwargs)
        # Add something
        pk = self.kwargs['pk']
        zmienna = Pokoj.objects.filter(id = pk)[0]
        context['nazwa_pokoju'] = zmienna.nazwa
        return context

def vote(self, pk):

    pokoj = Pokoj.objects.get(id = pk)
    osoba = self.user
    czlowiek = get_object_or_404(User, id = osoba.id)
    numerr = Numer.objects.filter(id_pokoj = pk).order_by('-id').values()[:1]
    if numerr:
        poprzednia_liczba = numerr[0]['numerek'] + 1
    else: 
        poprzednia_liczba = 1 
    #Warunek ile osob moze byc w jednej kolejce
    if poprzednia_liczba == 16:
        return render_to_response('pokoje/lista_pelna.html')
    czy_jest = Numer.objects.filter(id_pokoj = pk, id_user = czlowiek)
    if czy_jest:
        return render_to_response('pokoje/juzjest.html')
    
    Numer.objects.create(id_pokoj = pokoj, id_user = czlowiek, numerek = poprzednia_liczba)
    print "Pobrano numerek w pokoju: ",pokoj,"Uzytkownik: ",osoba,"Numer: ",poprzednia_liczba
    return HttpResponseRedirect("/") 

def zapisane_numery(request):
    czlowiek = request.user
    zapisane = Numer.objects.filter(id_user = czlowiek.id)
    #kategoria = Kategorie.objects.get(name)
    return render_to_response('pokoje/zapisane_numery.html',
                              #{'full_name': request.user.username},
                              {'zapisane': zapisane},
                              context_instance=RequestContext(request))


def cosik_pier(request):
    zapisane = Pokoj.objects.all()
    if request.POST:
        zapisane1 = Numer.objects.filter(id_pokoj= request.POST.get('choice', False))
    else:
        zapisane1 = 0
    return render_to_response('pokoje/cosik.html',
                              {'poll': zapisane, 'numer': zapisane1 },
                              context_instance=RequestContext(request))
