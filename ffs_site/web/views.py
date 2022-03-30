from csv import register_dialect
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from web.forms import loginForm, registerForm

def register_view(request):
    register_form = registerForm()
    if request.method == 'POST':
        register_form = registerForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            email = register_form.cleaned_data.get('email')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect(reverse('blog:dashboard', kwargs={'username': request.user.username}))
            else:
                print('User not found')
    return render(request, 'web/register.html', {'register_form':register_form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('blog:dashboard'))
    login_form = loginForm()
    if request.method == 'POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('blog:dashboard'))
            else:
                print('User not found')
    return render(request, 'web/login.html', {'login_form':login_form})

def logout_view(request):
    logout(request)
    return redirect(reverse('web:login'))
