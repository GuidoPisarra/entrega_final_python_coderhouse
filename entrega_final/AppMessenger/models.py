from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user_send = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    user_recept = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_received"
    )
    text = models.CharField(max_length=1000)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"user_send: {self.user_send} text: {self.text} user_recept : {self.user_recept}, check : {self.read}"
