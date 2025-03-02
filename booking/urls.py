from django.urls import path
from .views import register_view, login_view, logout_view,home_view
from .views import room_list, room_add, room_edit, room_delete
from .views import create_booking,booking_success
from .views import user_dashboard
from .views import booking_list,confirm_booking,cancel_booking
#from django.contrib.auth import views as auth_views #Он нужен, если используешь встроенные Django Views;Если уже написал свои представления (login_view, logout_view), то auth_views не нужен
urlpatterns = [
    path('home/', home_view, name='home'),  # Главная страница
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('rooms/', room_list, name='room_list'),
    path('rooms/add/', room_add, name='room_add'),
    path('rooms/edit/<int:pk>/', room_edit, name='room_edit'),
    path('rooms/delete/<int:pk>/', room_delete, name='room_delete'),
    path('booking/create/', create_booking, name='create_booking'),  # Страница бронирования
    path('booking/success/', booking_success, name='booking_success'),  # Страница успешного бронирования
    path("booking/dashboard/", user_dashboard, name="dashboard"),
        path("bookings/", booking_list, name="booking_list"),
    path("bookings/confirm/<int:pk>/", confirm_booking, name="confirm_booking"),
    path("bookings/cancel/<int:pk>/", cancel_booking, name="cancel_booking"),
]
