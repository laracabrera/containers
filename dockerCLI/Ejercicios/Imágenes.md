## Imágenes

Las imágenes son la base de Docker. Los contenedores se iniciarán a partir de ellas y representan una plantilla de solo lectura, que se crea incorporando los requisitos necesarios para cumplir el objetivo para el cual fue creada.

Vamos a empezar por tanto, a trabajar la busqueda de imágenes antes de instalar o desplegar ningun contenedor. Para ello, nos vamos al registro oficial [Docker Hub](https://hub.docker.com "Docker Hub") y vamos a buscar en este caso una imagen de *wordpress* preparada con la versión ***x.x.x-apache*** para poder realizar nuestra primera operación.

Una vez sepamos la versión de wordpress más reciente vamos a preparar el comando de instalación y para ello tenemos que pensar que queremos acceder a nuestro contenedor con wordpress desde fuera. Para ello vamos a agregar la opción -p de docker run, que nos permite publicar el puerto del contenedor y además asignarle uno en nuestra máquina, en este caso, el puerto de wordpress es el *80* y queremos vincularlo en el *8080*. Al final deberemos tener preparada una línea de comando como la siguiente:

`docker run -p <puertos> <imagen>`

Si la instalación ha sido correcta podemos acceder a nuestro wordpress directamente desde el navegador, con la siguiente URL:

[http://localhost:8080](http://localhost:8080 "http://localhost:8080")


### Gestión de imágenes

####Descarga

Las imagenes que nos descargamos se identifican, además de por el nombre, por una versión. De esa manera podemos tener distintas versiones de una misma imagen. Para usar una en concreto se utilizan los dos puntos seguido del nombre de la versión. Si no se indica nada, como hasta ahora, por defecto se descarga la etiquetada como latest.

Vamos a descargar alguna imagen más de docker, para ello utilizamos el comando *docker pull* , por ejemplo:

`docker pull wordpress:latest`

1. Utilizar docker pull para descargar varias imágenes diferentes, podeis consultar en Docker HUB.

####Listado y borrado

Para poder ver todas las imágenes que tenemos descargadas podemos hacer uso del comando docker images, un ejemplo es el siguiente:

```bash
$ docker images

REPOSITORY   TAG     IMAGE ID      CREATED      SIZE
wordpress    latest  ca0fefec932b  7 days ago   409MB
wordpress    php7.1  37664bd9863e  7 days ago   400MB
hello-world  latest  4ab4c602aa5e  2 weeks ago  1.84kB
```

Para terminar con el manejo de imágenes vamos a limpiar el ordenador de las diferentes imágenes descargadas usando el siguiente comando:

```bash
$ docker rmi wordpress:php7.1 

Untagged: wordpress:php7.1
Untagged: wordpress@sha256:2cc529d3d4a1308d6f5522422f4696d87267695f69702c
Deleted: sha256:37664bd9863efe67a83cb2ff293f1816a36b2af3d3b9f62d
Deleted::77c97f008777c89455c8e5f248a626b192b62cf07ed1993c9acdfab73be210ee
Deleted: sha256:14f58345b0bb2efaede03f9424412dc275343305a79952c9c8bda3d1ba
```

Consejo: Cuidado al eliminar imágenes que se están utilizando.

## Tareas

1. Repetir el proceso pero instalando un contendor con MySQL, prestar especial atención en la exposición de puertos.

2. Una vez conseguido el ejercicio 1, borrar todas las imágenes.

