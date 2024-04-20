from django import forms
from django.contrib.auth.models import User
from .models import Message


class New_message(forms.Form):
    user_recept = forms.IntegerField()
    text = forms.CharField(max_length=1500, widget=forms.Textarea)
