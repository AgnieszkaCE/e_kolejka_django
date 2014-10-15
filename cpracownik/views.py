from django.contrib.auth.models import Group
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import loader
from django.template.context import RequestContext
from django.views import generic

from cpracownik.forms import InfoForm
from cpracownik.models import Info
from pokoje.models import Numer
from pokoje.models import Pokoj


def w_grupie(request):
    grup = Group.objects.get(name='Pracownicy')
    user = request.user
    if grup in user.groups.all():
        prac = 1
    else:
        prac = 0
#kom
    return prac
    
def pracview(request):
    lista = Pokoj.objects.order_by('-nazwa')  
    pracownik = w_grupie(request)
    return render_to_response('cpracownik/pracList.html',
                              {'prac_list': lista, 'pracownik':pracownik},
                              context_instance=RequestContext(request))
          
def lista(request, pk):
    numer = Numer.objects.filter(id_pokoj = pk)
    pracownik = w_grupie(request)
    return render_to_response('cpracownik/deview_pracownik.html',
                              {'numer': numer, 'pracownik':pracownik},
                              context_instance=RequestContext(request)) 
    
def usuwa(request, idk):
    #poprawic 
    do_usuniecia = Numer.objects.filter(id = idk)[0]
    idd = do_usuniecia.id_pokoj
    id_danego_pokoju = Pokoj.objects.get(nazwa = idd)
    do_usuniecia.delete()
    #return HttpResponseRedirect('/pracownik/')
    return HttpResponseRedirect(reverse('cpracownik.views.lista', kwargs={'pk': id_danego_pokoju.id}))

def infoform(request):
    pracownik = w_grupie(request)
    if pracownik == 0:
        return render(request, 'index.html') 
    
    form = InfoForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        print "Dodano nowa informacje"
        save_it.save()
        
    return render_to_response('cpracownik/infoform.html',
                              locals(),
                              context_instance=RequestContext(request))

def infoview(request):
    info = Info.objects.order_by('-data') 
    pracownik = w_grupie(request)
    return render_to_response('cpracownik/infoList.html',
                              {'info_list': info, 'pracownik':pracownik},
                              context_instance=RequestContext(request))
    
def usunInfo(request, pk):
    #poprawic 
    do_usuniecia = Info.objects.filter(id = pk)
    #idd = do_usuniecia.id_pokoj
    do_usuniecia.delete()
    return HttpResponseRedirect('/pracownik/infoList/')
