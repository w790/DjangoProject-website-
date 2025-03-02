from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name="Номер комнаты")
    description = models.TextField(verbose_name="Описание")
    price_night = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена за ночь")
    image = models.ImageField(upload_to='room_images/', blank=True, null=True, verbose_name="Фото")
    def __str__(self):
        return f"Комната {self.number} - {self.price_night} руб/ночь"
class Booking(models.Model):
    STATUS_CHOICES = [
        ("Ожидание", "Ожидание"),
        ("Подтверждено", "Подтверждено"),
        ("Отменено", "Отменено"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Пользователь")
    room = models.ForeignKey(Room, on_delete=models.CASCADE,verbose_name="Комната")
    check_in = models.DateField(verbose_name="Дата заселения")
    check_out = models.DateField(verbose_name="Дата выселения")
    created_at  = models.DateTimeField(auto_now_add=True,verbose_name="Дата бронирования со временем")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Ожидание")  # Новое поле
    def __str__(self):
        return f"{self.user.username} забронировал комнату {self.room} с {self.check_in} по {self.check_out}"

    def is_available(self):
        """Проверяет, доступен ли номер для выбранных дат."""
        existing_bookings = Booking.objects.filter(room=self.room)
        for booking in existing_bookings:
            if (self.check_in < booking.check_out and self.check_out > booking.check_in):
                return False
        return True
