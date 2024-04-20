from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from AppBlog.models import *
from AppMessenger.forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required
def create_messege(request, id_post):
    if request.method == "GET":
        id_destinatario = Publication.objects.filter(id=id_post)
        destinatario = User.objects.filter(id=id_destinatario[0].user_id)
        return render(
            request,
            "new_message.html",
            {
                "destinatario": destinatario[0],
                "id_destinatario": id_destinatario[0].user_id,
                "id_post": id_post,
            },
        )
    else:
        form = New_message(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            destinatario = (
                User.objects.filter(id=data["user_recept"])
                .values_list("id", flat=True)
                .first()
            )
            new_mensaje = Message(
                text=data["text"],
                read=False,
                user_send=request.user,
                user_recept_id=data["user_recept"],
            )
            new_mensaje.save()
            return render(
                request, "home.html", {"mensaje": "El mensaje fue enviado con éxito."}
            )

    return render(request, "new_message.html", {"destinatario": ""})


def ver_mensajes(request):
    user = request.user
    print(user)
    mensajes = Message.objects.filter(user_recept=user, read=False)
    print(mensajes)

    return render(request, "my_messages.html", {"mensajes_no_leidos": mensajes})
