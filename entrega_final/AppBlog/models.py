from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    sub_title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="files", blank=True, null=True)

    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"image: {self.image} content: {self.content} date : {self.date_published}, user_id: {self.user.id}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"User: {self.user} imagen: {self.imagen}"
