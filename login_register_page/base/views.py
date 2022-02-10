from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm

def loginPage(request):
    if request.method == 'POST':
        email = LoginForm.email(request.POST)
        if email.is_valid():
            return HttpResponseRedirect('welcome/')
    
    context = {'email': email}
    return render(request, 'base/login.html', context) 
