# entrega_final_python_coderhouse

Proyecto final curso Coderhouse python, se deberá realizar una web similar a un blog con Django.

Se deberá de manera individual. Crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá admin, perfiles, registró, páginas y formularios.

La entrega se realizará enviando el link a GitHub, en el readme de Github deberá estar el nombre completo de los tres/dos participantes y una descripción de dos o tres renglones contando qué hizo cada uno.

En el github debe haber un video o link a vídeo donde nos muestran su web funcionando en no más de diez minutos.

Dentro del Github deberá existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados

Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejado en el route about/. (En castellano un “acerca de mí” que hable un poco de los creadores de la web y del proyecto).

Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog).

Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (O sea al hacer click se ve más detalle de lo que se veía en el apartado anterior).

Si no existe ninguna página mostrar un "No hay páginas aún". (Aclarando, si en la página hacemos clic en algún lugar que no existe que diga eso, o que lleve a un html con esos mensaje, no dejar botones que no responden).

Para crear, editar o borrar las fotos debes estar registrado como Administrador.

Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).

Si los estudiantes deciden resolverlo de manera grupal, deben avisar al tutor y enviarle los nombres de los estudiantes que conforman el grupo de trabajo. Luego, agregar una carátula o instancia en el PF con los nombres de los estudiantes.

Piezas sugeridas, no hace falta que estén todas, pero tiene que haber por lo menos un CRUD completo y el módulo de Login debe ser sólido:

NavBar Messages Create page
Home Profile Update Page
About Logout Delete page
Pages Get pages Get profile
Login Get page Update profile
Signup

Requisitos base

Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.

Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.

Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción - un link a una página web - email y contraseña.

Requisitos base

Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.

Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.

NOTA: No hace falta que sean APPs separadas, con dos APP estarán bien.

Recuerden que en la clase 1 tienen disponible un proyecto modelo de un ex estudiante para tomar como inspiración.

INICIO PROYECTO

# Creamos el proyecto

python -m django startproject entrega_final

Dentro de la carpeta entrega final creamos loas dos apps (blog y mensajería)

python manage.py startapp AppBlog
python manage.py startapp AppMessenger

respectivamente.

Realizamos la migración

python manage.py migrate

En la carpeta del proyecto, vamos al archivo settings.py para agregar ambas aplicaciones en INSTALLED_APPS

Luego, para corroborar que las aplicaciones se crearon correctamante, ejecutamos :

python manage.py check AppBlog
python manage.py check AppMensajería

Levantamos el servidor:

Corremos el servidor para corroborar que funciona

python manage.py runserver

En el archivo settings.py importamos
import os
from django.conf import settings

Para manejar los templates sin poner las rutar absolutas, configurándolo de esta manera:

<!-- TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(settings.BASE_DIR, "Appcoder", "template")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
] -->


