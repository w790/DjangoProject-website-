from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Room,Booking
# Форма для регистрации
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #указываем, какие поля хотим видеть в форме.

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields   = ['number', 'description', 'price_night', 'image'] #указываем, какие поля хотим видеть в форме.

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in >= check_out:
            raise forms.ValidationError("Дата выезда должна быть позже даты заезда.")

        if room:
            # Получаем пользователя, если он есть
            user = getattr(self.instance, 'user', None)
            # Проверим, доступен ли номер
            booking = Booking(user=user, room=room, check_in=check_in, check_out=check_out)
            if not booking.is_available():
                raise forms.ValidationError("Этот номер уже забронирован на выбранные даты.")

        return cleaned_data