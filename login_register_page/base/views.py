from turtle import pen
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate

from .forms import LoginForm, RegisterForm


def loginPage(request, emailreg=None, passwordreg=None):  
    if request.method == 'POST':
        print('!!')
        emaillog = request.POST['email']
        passwordlog = request.POST['password']
        loginform = LoginForm(request.POST)
        if loginform.is_valid:
            if emailreg == emaillog and passwordreg == passwordlog:
                return HttpResponseRedirect('welcome/')

    else:
        loginform = LoginForm()
    
    return render(request, 'base/login.html', {'loginform': loginform}) 


def registerPage(request):
    if request.method == 'POST':
        emailreg = request.POST['email']
        passwordreg = request.POST['password']
        loginPage(request, emailreg, passwordreg)
        return HttpResponseRedirect('http://127.0.0.1:8000/login')

    return render(request, 'base/register.html')      


def welcome(request):
    return render(request, 'base/welcome.html')
