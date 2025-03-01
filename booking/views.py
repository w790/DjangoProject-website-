from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm
from .forms import RoomForm
from .models import Room

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
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def logout_view(request):#Выхода пользователя из системы
    logout(request)
    return redirect('home')

# Представление для главной страницы
def home_view(request):
    return render(request, 'booking/home.html')

# Проверка: доступ только для администраторов
def admin_required(user):
    return user.is_staff

# Список всех номеров (только для администратора)
@login_required
@user_passes_test(admin_required)
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {'rooms': rooms})

# Добавление нового номера
@login_required
@user_passes_test(admin_required)
def room_add(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'booking/room_form.html', {'form': form})

# Редактирование номера
@login_required
@user_passes_test(admin_required)
def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'booking/room_form.html', {'form': form})

# Удаление номера
@login_required
@user_passes_test(admin_required)
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('room_list')