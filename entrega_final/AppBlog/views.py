from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from AppBlog.models import Publication
from AppBlog.forms import *


def inicio(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "register.html", {"mensaje": "Usuario creado"})
        else:
            return render(
                request, "register.html", {"form": form, "error": form.errors.as_text}
            )

    form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                print(user)
                return render(
                    request, "user_home.html", {"mensaje": f"Binevenid@ {usuario}"}
                )
            else:
                return HttpResponse(f"Usuario no encontrado.")
        else:
            return HttpResponse(f"Form incorrecto {form}")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def custom_logout(request):
    logout(request)
    return redirect("home")


def new_post(request):
    if request.method == "POST":
        mi_formulario = New_post(request.POST)
        print(mi_formulario.errors)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            print(request.user)
            nueva_publicacion = Publication(
                user=request.user,
                title=datos["title"],
                sub_title=datos["sub_title"],
                content=datos["content"],
                image=datos["image"],
            )

        # Redireccionar a una página de éxito o mostrar un mensaje
        return render(
            request, "new_post.html", {"mensaje": "Publicación creada exitosamente"}
        )

    # Si la petición no es un POST, renderizar el formulario para crear una publicación
    return render(request, "new_post.html")
