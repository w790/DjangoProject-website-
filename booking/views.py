from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm,BookingForm,RoomForm
from .models import Room
from .models import Booking

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

from django.contrib.auth.forms import AuthenticationForm

def login_view(request):  # Авторизация (вход) существующего пользователя
    form = AuthenticationForm()  #  Форма всегда создаётся

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Передаём данные в форму
        if form.is_valid():  #  Проверяем валидацию формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  #  Авторизуем пользователя
                return redirect('home')

    return render(request, 'booking/login.html', {'form': form})  #  Теперь `form` всегда определён


def logout_view(request):#Выхода пользователя из системы
    logout(request)
    return redirect('login')

# Представление для главной страницы
def home_view(request):
    rooms = Room.objects.all()  # Загружаем все номера из базы
    return render(request, 'booking/home.html',{'rooms': rooms})

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
            return redirect('booking/room_list')
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
            return redirect('booking/room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'booking/room_form.html', {'form': form})

# Удаление номера
@login_required
@user_passes_test(admin_required)
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('booking/room_list')


@login_required
def create_booking(request):
    print("Текущий пользователь:", request.user)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Устанавливаем текущего пользователя
            print("Перед сохранением: ", booking.user, booking.room, booking.check_in, booking.check_out)
            booking.save()
            return redirect('booking_success')  # Переход к успешному бронированию
    else:
        form = BookingForm()

    return render(request, 'booking/create_booking.html', {'form': form})

@login_required
def booking_success(request):
    return render(request, 'booking/booking_success.html')

@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user)  # Получаем бронирования текущего пользователя
    return render(request, "booking/dashboard.html", {"bookings": bookings})

# Проверяем, является ли пользователь администратором
def is_admin(user):
    return user.is_staff  # Только для админов

@login_required
@user_passes_test(is_admin)
def booking_list(request):
    bookings = Booking.objects.all()  # Получаем все бронирования
    return render(request, "booking/booking_list.html", {"bookings": bookings})

@login_required
@user_passes_test(is_admin)
def confirm_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = "Подтверждено"  # Меняем статус
    booking.save()
    return redirect("booking/booking_list")

@login_required
@user_passes_test(is_admin)
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = "Отменено"  # Меняем статус
    booking.save()
    return redirect("booking/booking_list")

@login_required
def user_cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status == "Ожидание":  # Пользователь может отменить только неподтвержденные бронирования
        booking.status = "Отменено"
        booking.save()
    return redirect("user_dashboard")