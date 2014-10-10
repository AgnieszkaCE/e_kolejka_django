from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from rejestracja.forms import FormRegister

def register_user(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('register_success')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = FormRegister()
    print args
    return render_to_response('registration/register.html', args)

def register_success(request):
    return render_to_response('registration/register_success.html')
