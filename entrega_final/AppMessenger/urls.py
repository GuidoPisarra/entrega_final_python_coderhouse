from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("create_messege/<int:id_post>", views.create_messege, name="create_messege"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
