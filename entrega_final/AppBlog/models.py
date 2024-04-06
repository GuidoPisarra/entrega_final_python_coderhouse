from django.db import models
from django.contrib.auth.models import User


def custom_upload_to(instance, filename):
    return f"assets/{filename}"  # Guarda los archivos en static/assets/


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    content = models.CharField(max_length=1000)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"image: {self.image} content: {self.content} date : {self.date_published}"
        )
