from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate

lista_email_pass = []


def loginPage(request, emailreg=None, passwordreg=None):
    if request.POST:
        lista_email_pass.append(emailreg)
        lista_email_pass.append(passwordreg) 
        emaillog = request.POST['email']
        passwordlog = request.POST['password']
        if lista_email_pass[0] == emaillog and  lista_email_pass[1] == passwordlog:
            return HttpResponseRedirect('http://127.0.0.1:8000/welcome')
        else:
            return HttpResponse('O email ou a password não correspondem tente novamente')
    
    return render(request, 'base/login.html') 


def registerPage(request):
    if request.POST:
        emailreg = request.POST['email']
        passwordreg = request.POST['password']
        loginPage(request, emailreg, passwordreg)
        return HttpResponseRedirect('http://127.0.0.1:8000')
        
    return render(request, 'base/register.html')      


def welcome(request):
    return render(request, 'base/welcome.html')