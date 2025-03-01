from django.urls import path
from .views import register_view, login_view, logout_view,home_view
from .views import room_list, room_add, room_edit, room_delete
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
]
