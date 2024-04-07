from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.inicio, name="home"),
    path("registro", views.register, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.custom_logout, name="logout"),
    path("new_post", views.new_post, name="new_post"),
    path("search_post", views.search_post, name="search_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
