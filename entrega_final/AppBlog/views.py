from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from AppBlog.models import Publication
from AppBlog.forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import AvatarForm


def inicio(request):
    publicaciones = Publication.objects.all()
    return render(
        request,
        "home.html",
        {"publicaciones": publicaciones, "MEDIA_URL": settings.MEDIA_URL},
    )


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
                # Asegurarse de pasar el objeto 'user' completo a Avatar
                avatar = Avatar.objects.get_or_create(user=user)[0]

                return render(
                    request,
                    "user_home.html",
                    {"mensaje": f"Bienvenid@ {user.username}", "avatar": avatar},
                )
            else:
                return HttpResponse("Usuario no encontrado.")
        else:
            return HttpResponse(f"Formulario incorrecto {form}")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def custom_logout(request):
    logout(request)
    return redirect("home")


@login_required
def new_post(request):
    if request.method == "POST":
        mi_formulario = New_post(request.POST, request.FILES)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            nueva_publicacion = Publication(
                user=request.user,
                title=datos["title"],
                sub_title=datos["sub_title"],
                content=datos["content"],
                image=datos["imagen"],
            )
            nueva_publicacion.save()
        # Redireccionar a una página de éxito o mostrar un mensaje
        return render(
            request, "new_post.html", {"mensaje": "Publicación creada exitosamente"}
        )

    # Si la petición no es un POST, renderizar el formulario para crear una publicación
    return render(request, "new_post.html")


def search_post(request):
    if request.method == "POST":
        mi_formulario = Form_search_post(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            publicaciones = (
                Publication.objects.filter(title__icontains=datos["search_post"])
                | Publication.objects.filter(sub_title__icontains=datos["search_post"])
                | Publication.objects.filter(content__icontains=datos["search_post"])
            )
            if len(publicaciones) > 0:
                return render(
                    request,
                    "home.html",
                    {"publicaciones": publicaciones, "MEDIA_URL": settings.MEDIA_URL},
                )
        else:
            return render(
                request,
                "home.html",
                {
                    "error": "No se encontraron publicaciones para su búsqueda.",
                    "MEDIA_URL": settings.MEDIA_URL,
                },
            )
    return render(
        request,
        "home.html",
        {
            "error": "No se encontraron publicaciones para su búsqueda.",
            "MEDIA_URL": settings.MEDIA_URL,
        },
    )


def search(request, id_post):
    if request.method == "GET":
        publicacion = Publication.objects.get(id=id_post)
        return render(
            request,
            "ver_mas_publicacion.html",
            {"publicacion": publicacion, "MEDIA_URL": settings.MEDIA_URL},
        )
    return render(
        request,
        "home.html",
        {
            "error": "No se encontraron publicaciones para su búsqueda.",
            "MEDIA_URL": settings.MEDIA_URL,
        },
    )


def about_us(request):
    publicaciones = Publication.objects.all()
    return render(
        request,
        "about.html",
    )


@login_required
def profile(request):
    usuario = request.user
    avatar = Avatar.objects.get_or_create(user=usuario)[0]

    if request.method == "POST":
        mi_formulario = User_edit_form(request.POST, instance=usuario)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if mi_formulario.is_valid() and avatar_form.is_valid():
            mi_formulario.save()
            avatar_form.save()
            return render(
                request,
                "profile.html",
                {
                    "mi_formulario": mi_formulario,
                    "avatar_form": avatar_form,
                    "usuario": usuario,
                    "avatar": avatar,
                },
            )

    else:
        mi_formulario = User_edit_form(instance=usuario)
        avatar_form = AvatarForm(instance=avatar)
        return render(
            request,
            "profile.html",
            {
                "mi_formulario": mi_formulario,
                "avatar_form": avatar_form,
                "usuario": usuario,
                "avatar": avatar,
            },
        )
    return render(
        request,
        "profile.html",
        {
            "mi_formulario": mi_formulario,
            "avatar_form": avatar_form,
            "usuario": usuario,
            "avatar": avatar,
        },
    )
