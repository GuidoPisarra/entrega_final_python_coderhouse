# Entrega final python coderhouse :computer:

## Alumno :student:

### Pisarra Guido

## Proyecto final curso Coderhouse python, se deberá realizar una web similar a un blog con Django.

- :boy: Se deberá de manera individual . Crearás una aplicación web estilo blog programada en Python :snake: en Django. Esta web tendrá admin, perfiles, registro, páginas y formularios.

- :paperclip: La entrega se realizará enviando el link a GitHub, en el readme de Github deberá estar el nombre completo de los tres/dos participantes y una descripción de dos o tres renglones contando qué hizo cada uno.

- :film_projector: En el github debe haber un video o link a vídeo donde nos muestran su web funcionando en no más de diez minutos.

- :file_folder: Dentro del Github deberá existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados

- :link: Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejado en el route about/. (En castellano un “acerca de mí” que hable un poco de los creadores de la web y del proyecto).

- :link: Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog).

- :open_book: Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (O sea al hacer click se ve más detalle de lo que se veía en el apartado anterior).

- :factory_worker: Para crear, editar o borrar las fotos debes estar registrado como Administrador.

- :scroll: Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).

## Piezas sugeridas, no hace falta que estén todas, pero tiene que haber por lo menos un CRUD completo y el módulo de Login debe ser sólido:

- NavBar Messages Create page

- Home

- Login

- Get page (Buscador)

- Update profile

- Signup

## Requisitos base

> Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.

> Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.

> Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/ o borrar: imagen - nombre - descripción - un link a una página web - email y contraseña.

> Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.

> Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.

> [!NOTE]
> NOTA: No hace falta que sean APPs separadas, con dos APP estarán bien.

# INICIO PROYECTO

## Creamos el proyecto

Los comandos utilizados para iniciar el proyecto son:

> python -m django startproject entrega_final

Dentro de la carpeta entrega final creamos loas dos apps (blog y mensajería)

> python manage.py startapp AppBlog
> python manage.py startapp AppMessenger

respectivamente.

## Realizamos la migración

> python manage.py migrate

En la carpeta del proyecto, vamos al archivo **settings.py** para agregar ambas aplicaciones en **INSTALLED_APPS**

Luego, para corroborar que las aplicaciones se crearon correctamante, ejecutamos :

> python manage.py check AppBlog
> python manage.py check AppMensajería

## Servidor:

Corremos el servidor para corroborar que funciona

> python manage.py runserver

En el archivo **settings.py** importamos

> import os from django.conf import settings

Para manejar los templates sin poner las rutar absolutas, configurándolo de esta manera:

```
TEMPLATES = [
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
]
```

- En la carpeta de la aplicación blog (que es la que haremos primeramente) agregamos la carpeta "static", y dentro de ella los archivos necesarios para que funcione bootstrap.

- Creamos dentro de la carpeta AppBlog una carpeta denominada template donde se encontrarán las plantillas html que utilizaremos.

- Creamos base.html que sera la base para las demás.

- En la carpeta de las aplicaciones creamos el archivo urls.py para manejar el routing que utilizaremos en las mismas
  Para que lo anterior quede bien configurado, debemos configurar en el archivo urls.py del proyecto (entrega_final), quedando éste, de esta manera:

```python
from django.contrib import admin
from django.urls import path, include
from AppBlog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", include("AppBlog.urls")),
]
```

> [!IMPORTANT]
> Una vez hecho esto, nos disponemos a desarrollar el blog, teniendo en cuenta que :

> - En el archivo urls de las aplicaciones vamos a definir las rutas de nuestro blog
> - En el archivo models de las aplicaciones vamos a definir los modelos que serán utilizados en nuestro blog
> - En el archivo forms de las aplicaciones vamos a definir los formularios que serán utilizados, de ser necesario, al cargar un formulario desde nuestro html
> - En el archivo views de las aplicaciones vamos a definir los vistas que serán utilizadas en nuestro blog

# Usuarios y autenticación

## ADMIN

> [!TIP]
> SuperUsuario
> user = giuliano
> pass = coder123

## Usuario común

> [!TIP]
> Usuario común
> usuario = pisarraguido@hotmail.com
> pass = guido1234
