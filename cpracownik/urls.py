from django.conf.urls import patterns, include, url

from cpracownik import views

 
urlpatterns = patterns('',
    #lista pokjow dla pracownikow
    #url(r'^$', views.PracView.as_view(), name='pracList'),
    url(r'^$', 'cpracownik.views.pracview', name='pracList'),
    url(r'^pracownik/(?P<pk>\d+)/$', 'cpracownik.views.lista', name = 'praclist'),
    url(r'^usun/(?P<idk>\d+)/$', 'cpracownik.views.usuwa', name = 'usun'),
    url(r'^infoform/$', 'cpracownik.views.infoform', name = 'form'),
    url(r'^infoList/$',  'cpracownik.views.infoview', name = 'infoList'),
    url(r'^usunInfo/(?P<pk>\d+)/$', 'cpracownik.views.usunInfo', name = 'usunInfo'),

)