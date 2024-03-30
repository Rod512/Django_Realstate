from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return HttpResponseRedirect('Home')

def register(request):
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
