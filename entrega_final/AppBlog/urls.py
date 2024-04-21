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
    path("about_us", views.about_us, name="about_us"),
    path("search_post", views.search_post, name="search_post"),
    path("search/<int:id_post>", views.search, name="search"),
    path("profile", views.profile, name="profile"),
    path("delete_image/<int:id_post>", views.delete_image, name="delete_image"),
    path("edit_image", views.edit_image, name="edit_image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
