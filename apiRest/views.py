from django.contrib.auth.models import User
from django.http.response import Http404
import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView

from apiRest.serializers import PokojSerializer
from pokoje.models import Pokoj, Numer


class PLista(APIView):
    def get(self, request, format=None):
        p = Pokoj.objects.all()
        serializer_pokoj = PokojSerializer(p)
        return Response(serializer_pokoj.data)
class PDetail(APIView):
    def get_object(self, pk):
        try:
            return Pokoj.objects.get(id=pk)
        except Pokoj.DoesNotExist:
            raise Http404
    def get(self, request, pk, format = None):
        p = self.get_object(pk)
        serializer_pokoje = PokojSerializer(p)
        return Response(serializer_pokoje.data)

class Pobierz_numerek(APIView):
    
    def get(self, request, p_nazwa, mail, format=None):
        user_ok = User.objects.get(username = mail)
        pokoj_ok = Pokoj.objects.get(nazwa = p_nazwa)    
        
        #Deklaracja zmiennej data, zmienna ta posiada komunikat zwrotny dla klienta
        data = {'stan': 0,
                'numer': 0
                } 
    
        if user_ok and pokoj_ok:
            czy_jest = Numer.objects.filter(id_pokoj = pokoj_ok, id_user = user_ok)
        else:
            
            data['stan'] = "Problem z wartosciami"
            return Response(data)
        
        numerr =  Numer.objects.filter(id_pokoj = pokoj_ok).order_by('-id').values()[:1]
        
        if czy_jest:
        
            data['stan'] =  "Posiadasz numerek"
            data['numer'] = numerr[0]['numerek']
            return Response(data)
        else: 
            if numerr:
                poprzednia_liczba = numerr[0]['numerek'] + 1
            else: 
                poprzednia_liczba = 1 
            
            Numer.objects.create(id_pokoj = pokoj_ok, id_user = user_ok, numerek = poprzednia_liczba)
            data['stan'] = "Pobrano numer"
            data['numer'] = poprzednia_liczba
            return Response(data)
        
class Numer_User(APIView):
    def get(self, request, p_nazwa, nazwaa, format=None):
        
        user_ok = User.objects.get(username = nazwaa)
        pokoj_ok = Pokoj.objects.get(nazwa = p_nazwa)    
        
        #Deklaracja zmiennej data, zmienna ta posiada komunikat zwrotny dla klienta
        data = {'stan': 0,
                'numer': 0,
                } 
        if user_ok and pokoj_ok:
            
            numer_user = Numer.objects.filter(id_pokoj = pokoj_ok, id_user = user_ok).order_by('-id').values()[:1]
            if numer_user:
                data['stan'] = "Posiadasz numerek"
                data['numer'] = numer_user[0]['numerek']
                return Response(data)   
            else:
                data['stan'] = "Nie Posiadasz"
               
                return Response(data)
class Login(APIView):
    def get(self, request, nazwa, haslo, format=None):
        
        data = {
                'stan': 0,
                'numer':0
                } 
       
        user = User.objects.get(username = nazwa)
  
        
        if user.check_password(haslo):
            data['stan'] = "Logged"
            return Response(data)
        else:
            data['stan'] = "Nie"
            return Response(data)

        
        