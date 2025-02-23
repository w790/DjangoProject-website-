from django.urls import path
from .views import register_view, login_view, logout_view
#from django.contrib.auth import views as auth_views #Он нужен, если используешь встроенные Django Views;Если уже написал свои представления (login_view, logout_view), то auth_views не нужен
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
