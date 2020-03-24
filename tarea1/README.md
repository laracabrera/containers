![logo UPM](./logo_upm.jpg) Especificación de un servicio
===================================================================

## Objetivo:

> El principal objetivo de esta tarea consiste en consolidar los conceptos relacionados con la especificación
> de un servicio. Para ello se definirá y publicará la definición de un servicio empleando el estándar
> [OpenAPI 3][openapi3]. Adicionalmente se simulará el comportamiento del servicio (se propone el empleo de
> [Spotlight Prism][prism], [Postman][postman], ...)

Enunciado:
----------

Para conseguir este objetivo se van a definir un conjunto de servicios que, posteriormente, se emplearán
para desarrollar una aplicación de gestión de un almacén de productos. En primer lugar se formarán equipos
de como máximo tres alumnos, y cada equipo deberá realizar la especificación de uno de los servicios propuestos.

Para publicar la especificación se deberá generar un contenedor docker que ofrezca la definición de las
operaciones disponibles en el servicio y describa las conexiones con otros servicios. Los servicios y las
diferentes funcionalidades que se deberán implementar deberán realizar las siguientes
funcionalidades completas:

    * Servicio 1: Gestión de Productos
        - Alta, baja y modificación de productos
        - Alta, baja y modificación de categorías
        - Búsqueda de productos con texto libre
        - Listado de productos de una categoría
        - Todas las operaciones son eventos a registrar

    * Servicio 2: Gestión de Pedidos
        - Alta, baja y modificación de pedidos
        - Búsqueda de pedidos por tipo, estado, producto, organización (cliente o proveedor) y texto libre
        - Consulta de stock de un producto (comprados y recibidos - vendidos y enviados o recibidos)
        - Todas las operaciones son eventos a registrar

    * Servicio 3: Registro de Eventos (logging)
        - Alta de eventos
        - Búsqueda de eventos por origen, nivel, rango de fechas y texto libre
        - Volcado en CSV de todos los eventos de un determinado origen
        - Todas las operaciones son eventos a registrar

    * Servicio 4: Facturación
        - Alta, baja y modificación de organizaciones
        - Alta y cancelación de facturas
        - La modificación de una factura implica baja de la misma y creación de una nueva con los cambios
        - Búsqueda de facturas por organización (cliente), rango de fecha, estado y texto libre
        - Todas las operaciones son eventos a registrar

### Esquemas:
- [Producto](./definitions/Producto.yaml)
- [Categoría](./definitions/Categoria.yaml)
- [Pedido](./definitions/Pedido.yaml)
- [Evento](./definitions/Evento.yaml)
- [Organización](./definitions/Organizacion.yaml) (proveedores, clientes, ...)
- [Factura](./definitions/Factura.yaml)

Notas:
------
1. En el diseño de cada servicio se tendrá en cuenta que cada uno de los servicios
   deberá contar con su propio mecanismo de persistencia
2. Se deberá enviar un único fichero comprimido en el que se adjuntarán todos
   los ficheros necesarios para desplegar el servicio asignado. Obligatoriamente
   se incluirá un Fichero `README.md` que contendrá las instrucciones necesarias para desplegar el proyecto desarrollado
3. Para realizar esta práctica se formarán grupos de 3 alumnos. Aquellos alumnos
   que opten por evaluación solo por prueba final realizarán el ejercicio de manera
   individual. En la plataforma se publicará el servicio asignado a cada alumno o
   grupo de alumnos.
        
[openapi3]: http://spec.openapis.org/oas/v3.0.3
[prism]: https://stoplight.io/open-source/prism/
[postman]: https://www.postman.com/