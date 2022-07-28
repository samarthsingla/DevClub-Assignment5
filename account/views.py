from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# Create your views here.
def login(request):
    return render(request, "account/login.html")


def register(request):
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('account-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form':form})

