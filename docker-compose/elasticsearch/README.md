# Stack para gestión de logs

![Elasticsearch](https://raw.githubusercontent.com/docker-library/docs/7baeec9386c1d3960fc9021a5973694b2e0e1af9/elasticsearch/logo.png) ![Logstash](https://raw.githubusercontent.com/docker-library/docs/0ec96bc990cb13028308932386c3820d0de5d3c1/logstash/logo.png) ![Kibana](https://raw.githubusercontent.com/docker-library/docs/7baeec9386c1d3960fc9021a5973694b2e0e1af9/kibana/logo.png)

El objetivo de este taller es desplegar un sistema para la gestión de logs formado por los siguientes servicios:

- [Elasticsearch](https://www.elastic.co/es/elasticsearch/) es un motor de búsqueda y analítica de RESTful distribuido capaz de abordar un número creciente de casos de uso. Como núcleo del Elastic Stack, almacena de forma central tus datos para una búsqueda a la velocidad de la luz, relevancia refinada y analíticas poderosas que escalan con facilidad.
- [Logstash](https://www.elastic.co/products/logstash) es un pipeline de procesamiento de datos gratuito y abierto del lado del servidor que ingesta datos de una multitud de fuentes, los transforma y luego los envía a tu "escondite" favorito.
- [Kibana](https://www.elastic.co/es/kibana/) es una interfaz de usuario gratuita y abierta que te permite visualizar los datos de Elasticsearch y navegar en el Elastic Stack. Realiza lo que desees, desde rastrear la carga de búsqueda hasta comprender la forma en que las solicitudes fluyen por tus apps.

Cada uno de estos servicios tiene su imagen de contenedor oficial en **Docker Hub**. Para ver el *stack* en funcionamiento vamos a utilizar unos logs pre-generados de un servidor web de **NGINX** (fichero `nginx.log` en este mismo repositorio). Estos logs deben ser accesibles por el servicio **Logstash**. Para no tener que aprender a usar este servicio, también se proporciona el fichero de configuración pertinente para interpretar los logs de **NGINX** (el fichero `logstash-nginx.config` es la configuración del *pipeline* para **Logstash**).

## Tareas

1. Crea el fichero `docker-compose.yml` con toda la infraestructura necesaria para ejecutar el stack Elasticsearch + Logstash + Kibana.
2. Asegúrate de que el servicio Logstash tiene acceso a los ficheros `nginx.log` y `logstash-nginx.log`.
3. Conecta todos los servicios a una misma red virtual (ponle el nombre que quieras).
4. Asegúrate de exponer puertos públicos del *host* a cada uno de los servicios, se puede acceder a todos ellos de manera independiente con el navegador:
	- Elasticsearch da servicio en el puerto 9200
	- Logstash da servicio en el puerto 9600
	- Kibana da servicio en el puerto 5601
