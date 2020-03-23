
FROM php:7.2-apache

# Icecoder necesita este modulo de Apache para funcionar
RUN a2enmod rewrite
# Necesitamos la utilizad para descomprimir ficheros .zip
RUN apt-get update && apt-get install unzip

# Descargamos el .zip de Icecoder
ADD https://icecoder.net/download-zip /var/www/html/icecoder.zip
RUN cd /var/www/html && unzip -o  icecoder.zip && mv ICEco* icecoder

# Damos permiso de escritura a los directorios segun se indica en las instrucciones de instalacion de Icecoder
RUN chmod +w -R /var/www/html/icecoder/lib /var/www/html/icecoder/data /var/www/html/icecoder/plugins /var/www/html/icecoder/tmp
# Y cambiamos al propietario para que no haya problemas con la sesion
RUN chown -R www-data:www-data /var/www/html
