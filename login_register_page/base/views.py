from turtle import pen
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate

from .forms import LoginForm, RegisterForm


def loginPage(request, emailreg=None, passwordreg=None):  
    print(emailreg)
    if request.method == 'POST':
        emaillog = request.POST['email']
        passwordlog = request.POST['password']
        loginform = LoginForm(request.POST)
        '''
        if form.is_valid:
            if emailreg == emaillog and passwordreg == passwordlog:
                return HttpResponseRedirect('welcome/')
        '''
    else:
        loginform = LoginForm()
    
    return render(request, 'base/login.html', {'loginform': loginform}) 


def registerPage(request):
    if request.method == 'POST':
        emailreg = request.POST['email']
        passwordreg = request.POST['password']
        registerform = RegisterForm(request.POST)
        loginPage(request, emailreg, passwordreg)

    context = {'registerform': registerform}

    return render(request, 'base/register.html', context)      


def welcome(request):
    return render(request, 'base/welcome.html')
