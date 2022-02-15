# Ejercicio de WordPress en Docker CLI

Queremos levantar un servicio de WordPress pero para ello necesitamos vincularle una Base de Datos persistente.

## Creación del contenedor  para la BD

Por defecto, WordPress soporta los motores de MariaDB y MySQL, por lo que no tendremos muchos problemas para configurarlo.
Un ejemplo que nos sirva de referencia para configurar el contenedor para la base de datos de WordPress es:

```bash
docker run -d --name wordpress-db \
    --mount source=wordpress-db,target=/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=wordpress \
    -e MYSQL_USER=manager \
    -e MYSQL_PASSWORD=secret mariadb:10.3.9
```

Dentro de la configuración tenemos los siguientes parámetros:
 - `-d` permite ejecutar docker run en background lo que hace que podamos seguir ejecutando comandos en la terminal.
 - Por defecto, si ejecutamos `docker ps` veremos que se ha establecido el puerto 3306/tcp pero no está publicado en nuestra máquina. Por lo que el único capaz de acceder a la BD será el contenedor.
 - `- e` permite introducir datos de configuración a la BD del contenedor. Es decir, hemos configurados las variables predefinidad en la BD.
 - `--mount` nos permite enlazar un volumen creado (en este caso `/var/lib/mysql`), de esta manera todos los datos de la BD quedarán almacenados allí.

### Contenedor de WordPress

Vamos a crear otra vez un contenedor de WordPress, pero tenemos que vincularlo a la BD que se ha creado. Además, queremos poder editar los ficheros de las plantillas, por si tenemos que modificar algo, así que necesitaremos montar el directorio del contenedor donde está instalado WordPress con nuestra cuenta de usuario en la máquina anfitrión.

Para el directorio del espacio de trabajo:

```bash
mkdir -p ~/Sites/wordpress/target && cd ~/Sites/wordpress
```
Y dentro del directorio arrancamos el contenedor:
```bash
docker run -d --name wordpress \
    --link wordpress-db:mysql \
    --mount type=bind,source="$(pwd)"/target,target=/var/www/html \
    -e WORDPRESS_DB_USER=manager \
    -e WORDPRESS_DB_PASSWORD=secret \
    -p 8080:80 \
    wordpress:4.9.8
```

Para comprobar que se ha generado correctamente [http://localhost:8080](http://localhost:8080 "http://localhost:8080")

## Tareas
1. Crea correctamente los volúmenes y el directorio de trabajo donde corresponda.
2. Con las instrucciones mostradas anteriormente, levanta el servicio de WordPress cambiando las credenciales de acceso a la BD.
