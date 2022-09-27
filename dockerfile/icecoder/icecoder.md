# IDE web Icecoder

![Icecoder logo]([https://assets.icecoder.net/images/icecoder.png](https://assets.icecoder.net/images/icecoder.png))

[Icecoder](https://icecoder.net) es un entorno integrado de desarrollo (IDE) accesible a través de la web mediante un navegador. Según su web oficial:

> ICEcoder is a browser based code editor, which provides a modern approach to building websites. By allowing you to code directly within the web browser, online or offline, it means you only need one program (your browser) to develop sites, plus can test on actual web servers. After development, you can also maintain the website easily, all of which make for speedy and smart development.

## Objetivo

El objetivo de este problema es crear una imagen Docker con el entorno integrado de desarrollo **ICEcoder**.

Por lo tanto, el objetivo del problema pasa por diseñar el fichero [Dockerfile](https://docs.docker.com/engine/reference/builder/) necesario para que **ICEcoder** se pueda desplegar en un contenedor Docker.

Para construir el Dockerfile debes basarte en los requisitos e instrucciones de instalación que puedes encontrar en su [manual](https://icecoder.net/manual) y se resumen en:

### Requisitos

* Servidor web Apache o similar (Nginx)

* PHP 7.0 como mínimo

### Instalación

1. Descargar el ZIP desde la web oficial (recuerda que `ADD` permitía pasar una URL como parámetro).

2. Descomprimir el fichero en una ruta accesible por el servidor web.

3. Dar permisos de escritura a las carpetas `data`, `lib`, `plugins` y `tmp`.

4. Acceder al servidor desde el navegador para establecer la contraseña.
