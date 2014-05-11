from django.conf.urls import patterns, include, url

from numer import views

urlpatterns = patterns('',
    url(r'^$', views.ZapisView.as_view(), name='numer'),
    url(r'^pobierz/$', 'numer.views.pobieranienu'),
    
)