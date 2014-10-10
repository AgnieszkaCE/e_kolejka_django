from django.conf.urls import patterns, include, url
from apiRest import views
from rest_framework.urlpatterns import format_suffix_patterns
import apiRest



urlpatterns = patterns('',
   
  
    url(r'^$', views.PLista.as_view(), name='ListaLIsta'),     
    url(r'^d/(?P<pk>\d+)/$', views.PDetail.as_view()), 
    url(r'^stan/(?P<p_nazwa>[0-9a-zA-Z  _-]+)/(?P<nazwaa>\w+)/$', views.Numer_User.as_view(), name = 'Numer'),
    url(r'^kolejka/(?P<p_nazwa>[0-9a-zA-Z  _-]+)/(?P<mail>\w+)/$', views.Pobierz_numerek.as_view()), 
    url(r'^login/(?P<nazwa>[0-9a-zA-Z  _-]+)/(?P<haslo>[0-9a-zA-Z  _-]+)/$', apiRest.views.Login.as_view()), 

    
    
    
)

urlpatterns = format_suffix_patterns(urlpatterns) 