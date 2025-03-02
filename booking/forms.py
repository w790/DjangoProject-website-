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
            raise forms.ValidationError("Check-out date must be after check-in date.")

        if room:
            # Проверим, доступен ли номер
            booking = Booking(user=self.instance.user, room=room, check_in=check_in, check_out=check_out)
            if not booking.is_available():
                raise forms.ValidationError("This room is already booked for the selected dates.")

        return cleaned_data