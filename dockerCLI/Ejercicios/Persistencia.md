## Persistencia de datos

Por defecto, cualquier contenedor que se cree está aislado del resto. De esta manera, se puede vincular un contenedor a un puerto de red para poder acceder a él y eso incluye al sistema de archivos que contiene.

No obstante, cuando borremos el contenedor borraremos sus datos. Si queremos almacenar datos (una web, una base de datos, etc.) dentro de un contenedor necesitamos una manera de almacenarlos sin perderlos.

Docker ofrece tres maneras:

 - A través de volúmenes, que son objetos de Docker como las imágenes y los contenedores.
 - Montando un directorio de la máquina anfitrión dentro del contenedor.
 - Almacenándolo en la memoria del sistema (aunque también se perderían al reiniciar el servidor).

Al final la mejor forma es usar volúmenes, pero habrá ocasiones en que es preferible montar directamente un directorio de nuestro espacio de trabajo. Por ejemplo, para guardar los datos de una base de datos usaremos volúmenes, pero para guardar el código de una aplicación o de una página web montaremos el directorio.


### Crear volúmenes

Vamos a empezar usando la creación de volumenes para una BD de Wordpress:

```bash
$ docker volume create wordpress-db
```

### Lista de los volúmenes

Para visualizar los volúmenes disponibles usamos el siguiente comando:

```bash
$ docker volume ls

DRIVER              VOLUME NAME
local                   wordpress-db
```

### Información de cada volúmen

Los volumenes se crean en un directorio del sistema por defecto y no es recomendable acceder a él, y menos aún si existe un contenedor usándolo. No obstante, podemos visualizar los metadatos usando el comando `docker inspect` como por ejemplo:

```bash
$ docker volume inspect wordpress-db 
[
    {
        "CreatedAt": "yyyy-mm-ddThh:ii:ss+Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/wordpress-db/_data",
        "Name": "wordpress-db",
        "Options": {},
        "Scope": "local"
    }
]
```

### Borrado de volúmenes

Como con todos los objetos de Docker, los volúmenes pueden pasar a mejor vida, y para ello podemos hacer uso del comando `docker volume rm <nombre_contenedor>`.
