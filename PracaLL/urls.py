from django.conf.urls import patterns, include, url
from django.contrib import admin
from pokoje import views

admin.autodiscover()
 
urlpatterns = patterns('',
    #Admin
    url(r'^admin/', include(admin.site.urls)), 
    #Strona glowna 
    url(r'^$', views.Index.as_view(), name='index'),         
    #Logowanie
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'logowanie.views.logoutview'),
    #rejestracja
    url(r'^register/$', 'rejestracja.views.register_user'),
    url(r'^register/register_success/$', 'rejestracja.views.register_success'),
    #pokoj, numerki 
    url(r'^pokoj/$', views.PokojView.as_view(), name='pokoje'),
    url(r'^(?P<pk>\d+)/$', views.NumerView.as_view(), name='numer'),
    url(r'^(?P<pk>\d+)/vote/$', 'pokoje.views.vote', name='vote'),
    url(r'^zapisane/$', 'pokoje.views.zapisane_numery', name='zapisane'),
    #url pracownikow
    url(r'^pracownik/',include('cpracownik.urls')),
    url(r'^api/',include('apiRest.urls')),
    url(r'^cosik/$', 'pokoje.views.cosik_pier', name='ok'),
    
 
    
)
