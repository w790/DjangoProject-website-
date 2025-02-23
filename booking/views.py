from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Форма — это основа ввода данных.
# Форма регистрации — это интерфейс, с помощью которого пользователи будут вводить свои данные

def register_view(request):#Регистрация нового пользователя
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,"booking/register.html",{'form':form})
def login_view(request):#Авторизация (вход) существующего пользователя
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('home')
def logout_view(request):#Выхода пользователя из системы
    logout(request)
    return redirect('home')