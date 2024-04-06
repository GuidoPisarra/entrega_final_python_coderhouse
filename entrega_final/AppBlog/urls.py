from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("registro", views.register, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.custom_logout, name="logout"),
]
