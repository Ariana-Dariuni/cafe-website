from django.shortcuts import render, redirect # type:ignore
from django.contrib.auth import authenticate, login, logout # type:ignore
from django.contrib import messages # type:ignore
from django.contrib.auth.forms import UserCreationForm # type:ignore


def home(request):
    return render(request, 'cafe/home.html' )

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'admin' and password == 'admin':
            return redirect('management')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'cafe/login.html')

def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cafe/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def Management(request):
    return render(request, 'cafe/management.html')