from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from logowanie.models import Logowanie


def logoutview(request):
    logout(request)
    return render(request, 'registration/logout.html')

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ListContactView(LoggedInMixin, ListView):

    model = Logowanie
    template_name = 'index.html'

    def get_queryset(self):

        return Logowanie.objects.filter(owner=self.request.user)

class ContactView(LoggedInMixin, DetailView):

    model = Logowanie
    template_name = 'index.html'


    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})

        return obj 
    
