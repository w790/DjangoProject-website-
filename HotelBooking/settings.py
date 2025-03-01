# settings.py

import os
from pathlib import Path

# Основные настройки проекта
BASE_DIR = Path(__file__).resolve().parent.parent  # Корень проекта
SECRET_KEY = 'your-secret-key'  # Секретный ключ, не размещайте в открытых репозиториях
DEBUG = True  # Режим отладки
ALLOWED_HOSTS = []  # Список разрешённых хостов

# Приложения проекта
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',  # Ваше приложение
]

# Мидлвары
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL конфигурации
ROOT_URLCONF = 'HotelBooking.urls'

# Конфигурация шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Убедитесь, что указали путь к папке с шаблонами
        'APP_DIRS': True,  # Использование шаблонов в директориях приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Включение базы данных SQLite (или PostgreSQL, если вы используете её)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки для статических файлов (CSS, JavaScript, изображения)
STATIC_URL = '/static/'

# Настройки для медиа файлов (если они есть)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Установка языковых и часовых настроек
LANGUAGE_CODE = 'ru-ru'  # Язык
TIME_ZONE = 'Europe/Moscow'  # Часовой пояс
USE_I18N = True
USE_L10N = True
USE_TZ = True
