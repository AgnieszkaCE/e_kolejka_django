from django.conf.urls import patterns, include, url
from django.contrib import admin
from pokoje import views




admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)), 
    #Strona glowna
    url(r'^$', 'logowanie.views.index'), 
              
    #Logowanie
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'logowanie.views.logoutview'),
    
    #od pokoju 
    url(r'^pokoj/$', views.PokojView.as_view(), name='pokoje'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^numer/$', views.NumerView.as_view(), name='numer'),
    #url(r'^numerrk/(?P<pk>\d+)/$', views.DetailNView.as_view(), name='numerrrek'),
    url(r'^ok/$', 'pokoje.views.numerek')
    #url(r'^numer/', include('numer.urls')),
    
    
    
)