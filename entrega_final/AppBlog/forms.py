from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]


class New_post(forms.Form):
    title = forms.CharField(max_length=30)
    sub_title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=1500, widget=forms.Textarea)
    imagen = forms.ImageField(required=False)


class Form_search_post(forms.Form):
    search_post = forms.CharField(max_length=100)


class User_edit_form(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(
        label="Ingrese la nueva contraseña", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_text = {k: "" for k in fields}


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]


class Edit_image(forms.Form):
    id_publicacion = forms.IntegerField()
    imagen = forms.ImageField(required=False)
