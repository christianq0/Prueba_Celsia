# Prueba_Celsia
Descripción Alto Nivel

Es importante anotar que para un rango de fechas se puede tener el valor de energía, es un valor que se va acumulando.
El valor de potencia activa es un valor instantáneo, por lo que solo se podría tener para una fecha especifica o definir si se va a sacar un promedio para un rango de fechas dada.

Así pues, aunque tenemos valores de potencia activa desde el medidor, se tomará medida como el valor de energía. 

Captura de datos-
Se requiere implementar un proceso de carga masiva de lecturas por dispositivo.
En este punto se entiende que los medidores están conectados a una RTU/Servidor por medio de protocolo Modbus, que entrega las mediciones de los dispositivos cada hora y son exportados en archivos separados por comas.

Para implementar el servicio de lectura de datos se utilizará una librería de Python para leer y procesar los datos de los archivos .CSV

Para implementar el servicio de carga masiva de lecturas se hará uso de la herramienta Apache Spark.


Base de datos de clientes-
Se debe implementar una base de datos de clientes que permita tener almacenadas las credenciales de usuario de cada uno de ellos.
Se implementará una base de datos en MySQL o PostgreSQL dependiendo de la proyección a futuro del número de clientes


Diseño de UX-

El diseño de la interfaz de usuario debe permitir a los usuarios autenticarse en el sistema y consultar las medidas de algún dispositivo de medida en un rango de fechas dado.
Se utilizará React  para desarrollar la interfaz de usuario y Spring para la implementación de microservicios y rest.

