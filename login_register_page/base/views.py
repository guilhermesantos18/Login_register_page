from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm



def loginPage(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('welcome/')
    
    else:
        form = LoginForm()
    

    return render(request, 'base/login.html', {'form': form}) 


def registerPage(request):
    return render(request, 'base/register.html')      


def welcome(request):
    return render(request, 'base/welcome.html')
