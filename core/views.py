from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from nightmare.models import Nightmare

from core.forms import RegisterForm, LoginForm


def home(request, statut=None):
    print("home")
    last_nightmare = Nightmare.objects.last()
    return render(request, 'core/home.html', locals())


def core_register(request):
    print("register")
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        password_confirm = form.cleaned_data.get('confirm_password')
        user = User.objects.create_user(username=username, password=password)
        return redirect(reverse('core_home', args=['register_success']))

    return render(request, 'core/register.html', locals())


def core_login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect(reverse('core_home', args=['login_success']))
    return render(request, 'core/login.html', locals())


def core_logout(request):
    logout(request)
    return redirect(reverse('core_home', args=['logout_success']))
