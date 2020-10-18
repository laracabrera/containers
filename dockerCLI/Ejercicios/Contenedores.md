## Contenedores

Los contenedores son instancias de las imagenes que se crean durante la instalación con las imágenes que se descargan previamente.

### Listado

Para visualizar un listado de contenedores que tenemos en el sistema podemos hacer uso de `docker container ls` o utilizar `docker ps`. No obstante, cada comando tiene su particularidad. Un ejemplo de ejecución sería:

```bash
$ docker container ls -a

CONTAINER ID  IMAGE        COMMAND     CREATED         STATUS      PORTS  NAMES
4bd76e08b07f  wordpress    "docker-…"  11 minutes ago  Exited (0)         peaceful_murdock
69a3c34c224d  hello-world  "/hello"    18 minutes ago  Exited (0)         blissful_goldwasser
```

### Operaciones básicas sobre un contenedor

###### Iniciar contenedor
Para poder trabajar con los contendores que tenemos instalados, podemos usar el comando `docker container start <nombre_contenedor>` e iniciaremos el contenedor:

```bash
$ docker container start peaceful_murdock 

$ docker ps

CONTAINER ID  IMAGE      COMMAND    CREATED         STATUS  PORTS                 NAMES
4bd76e08b07f  wordpress  "docker…"  14 minutes ago  Up      0.0.0.0:8080->80/tcp  peaceful_murdock
```
###### Detener contenedor
Con un contenedor ejecutandose podemos detenerlo usando el comando `docker container stop <nombre_contenedor`, como se muestra a continuación:

```bash

$ docker container stop 4bd76e08b07f
4bd76e08b07f
```
Nota: Se puede usar el nombre del contenedor o su ID.

###### Borrar contenedor

Obviamente un contenedor ocupa espacio en la máquina, y además puededar lugar a confusión si tenemos demasiados contenedores. Por ello es interesante conocer como borrar un contenedor. En este caso haremos uso del comando `docker container rm <nombre_contenedor`, un ejemplo sería:

```bash
$ docker container rm 4bd76e08b07f
4bd76e08b07f
```

### Ejecutar comandos dentro de un contenedor

En ejercicios anteriores hemos visto como utilizar `docker run` para crear un contenedor desde una imágen, pero tambien podemos utilizar este comando con diferentes opciones para poder acceder al contenedor y ejecutar comandos, por ejemplo:

```bash
docker run --name ubuntu_bash --rm -i -t ubuntu bash
```

------------
###### Información adicional

Las primeras versiones de Docker eran más limitadas respecto a la creación de objetos. Así que con el tiempo se incorporaron comandos como `docker start`, `docker stop`, etc. relacionados con los contenedores.

Así que se ha creado una jerarquía nueva de subcomandos bajo el comando container que son equivalentes y se mantienen por compatibilidad:

|Antiguo   | Nuevo  |
| :------------ | :------------ |
| `docker run`  | `docker container run`  |
| `docker start`  | `docker container start`  |
| `docker stop`  | `docker container stop`  |
| `docker rm`  | `docker container rm`  |
| `docker inspect`  | `docker container inspect`  |
| `docker exec`  | `docker container exec`  |


------------

No obstante, mediante `docker run` solo se puede ejecutar al crear un nuevo contenedor, por lo que, no podremos usarlo una vez que ya esté creado el contenedor. Para ello debemos hacer uso de otro comando, `docker container exec`.

```bash
docker exec -w /tmp ubuntu_bash touch my_file.sh
```

En este caso, el parámetro `-w` indica el directorio de trabajo, luego viene el nombre del contenedor (`ubuntu_bash`) y por último el comando a ejecutar (`touch my_file.sh`)

#### Ejercicio
1. Instalar un nuevo contenedor de ubuntu y en el comando de ejecución añadir la opción pertinente para abrir a bash del contenedor. (mantener abierta esta ejecución).
2. En otro terminal, usar el comando necesario para en ese mismo contenedor ejecutar un comando que en el directorio `/temp` genere un nuevo archivo como un `echo 'hola mundo'`.
3. Verificar con la primera terminal que el archivo ha sido creado.
4. Detener la ejecución de todos los contenedores y borrarlos.
