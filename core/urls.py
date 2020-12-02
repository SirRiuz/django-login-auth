
from django.contrib import admin
from django.urls import path
from .views import index
from accounts.views import (login,register)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', login),
    path('auth/register/', register),
    path('', index),
]
