from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.

def index(request):
    return render(request, "index.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Failed to Login')
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})
