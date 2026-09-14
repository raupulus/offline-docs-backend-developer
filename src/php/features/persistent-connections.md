---
title: Conexiones persistentes a bases de datos
source_url: https://www.php.net/manual/es/features.persistent-connections.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/persistent-connections.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_reviewed: false
translation_revision: ee5ee8401
order: 1590
---

## Conexiones persistentes a bases de datos

## ¿Qué son las conexiones persistentes?

Las conexiones persistentes son enlaces que no se cierran al finalizar la ejecución de un script. Cuando se solicita una conexión persistente, PHP comprueba si ya hay una idéntica (que ya estuviera abierta antes), utilizándola si existe. Si no, crea el enlace. Una conexión «idéntica» es una conexión que fue abierta por el mismo host, con el mismo usuario y la misma contraseña (donde sea aplicable).

No hay ningún método para solicitar una conexión específica, o garantizar si obtendrá una conexión existente o una nueva (si todas las conexiones existentes están en uso, o la solicitud está siendo atendida por un trabajador diferente, el cual tiene un grupo separado de conexiones).

Esto significa que no puedes usar las conexiones persistentes de PHP para, por ejemplo:

asignar una sesión de base de datos específica a un usuario web específico

crear una transacción grande en múltiples solicitudes

iniciar una consulta en una solicitud y recopilar los resultados en otra

Las conexiones persistentes no le brindan *ninguna* funcionalidad que no fuera posible con las conexiones no persistentes.

## Solicitudes web

Hay dos formas las cuales su servidor web puede utilizar PHP para generar páginas web:

El primer método es emplear PHP como una «envoltura» CGI. Cuando se ejecuta de esta forma, se crea y se destruye una instancia del intérprete de PHP por cada solicitud de página (para una página de PHP) al servidor web. Debido a que esta instancia se destruye después de cada solicitud, cualquier recurso que adquiera (tal como un enlace a un servidor de base de datos SQL) es cerrado en la destrucción de dicha instancia. En este caso, no se gana nada utilizando conexiones persistentes: simplemente no persisten.

El segundo método, y más popular, es ejecutar PHP-FPM, o PHP como módulo en un servidor web multiproceso, lo que actualmente solo incluye a Apache. Estas configuraciones suelen tener un proceso (el padre) que coordina un grupo de procesos (sus hijos) los cuales son los que realmente hacen el trabajo de servir páginas web. Cuando una solicitud proviene de un cliente, esta es cedida a uno de los hijos que no esté ya sirviendo a otro cliente. Esto significa que cuando el mismo cliente hace una segunda solicitud al servidor, esta podría ser servida por un proceso hijo diferente a la primera vez. Una vez que se ha abierto una conexión persistente, cualquier solicitud posterior servida por el mismo proceso hijo puede reusar la conexión ya establecida al servidor SQL.

> [!NOTE]
> Puede comprobar qué método utilizan sus solicitudes web consultando el valor de "Server API" en la salida de `phpinfo` o el valor de `PHP_SAPI`, ejecutado desde una solicitud web.
>
> Si la API del servidor es "Apache 2 Handler" o "FPM/FastCGI", se usarán conexiones persistentes en todas las solicitudes atendidas por el mismo trabajador. Con cualquier otro valor, las conexiones persistentes no persistirán después de cada solicitud.

## Procesos de línea de comandos

Dado que PHP de línea de comandos utiliza un nuevo proceso para cada script, las conexiones persistentes no se comparten entre scripts de línea de comandos, por lo que no tiene sentido usarlas en scripts transitorios como crons o comandos. Sin embargo, pueden ser útiles si, por ejemplo, se está desarrollando un servidor de aplicaciones de larga duración que atiende muchas solicitudes o tareas, y cada una puede necesitar su propia conexión a la base de datos.

## ¿Por qué usarlas?

Las conexiones persistentes son recomendables si la sobrecarga para crear un enlace a su servidor SQL es alta. Que esta sobrecarga sea realmente alta o no depende de muchos factores, como el tipo de base de datos que se emplea, si esta se encuentra en la misma computadora en la que está el servidor web, la carga de la máquina donde está el servidor SQL, etc. En resumidas cuentas, si la sobrecarga de una conexión es alta, las conexiones persistentes ayudan considerablemente, haciendo que un proceso hijo únicamente se conecte una vez durante su vida útil, en lugar de hacerlo cada vez que procese una página que requiera una conexión al servidor SQL. Esto significa que cada hijo que abra una conexión persistente tendrá su propia conexión persistente abierta al servidor. Por ejemplo, si se tienen 20 procesos hijos diferentes que ejecutan un script que realiza una conexión persistente al servidor SQL, se tendrán 20 conexiones diferentes al servidor SQL, una por cada hijo.

## Posibles inconvenientes: Límites de conexión

Observe, sin embargo, que esto puede tener algunos inconvenientes si se está usando una base de datos con un limite de conexiones que sea excedido por las conexiones persistentes hijas. Si la base de datos tiene un limite de 16 conexiones simultáneas, y en el curso de una sesión de un servidor ocupado 17 hilos hijos intentan conectarse, uno de ellos no será capaz de hacerlo. Si un script contiene errores que impidan el cierre de las conexiones (como un bucle infinito), la mencionada base de datos con solamente 16 conexiones podría saturarse rápidamente.

Las conexiones persistentes suelen aumentar el número de conexiones abiertas en un momento dado, ya que los procesos inactivos mantienen las conexiones utilizadas en las solicitudes anteriores que atendieron. Si se inicia un gran número de procesos para manejar una oleada de solicitudes, las conexiones que estos abrieron permanecerán activas hasta que el proceso sea finalizado o el servidor de base de datos cierre la conexión.

Asegúrate de que el número máximo de conexiones permitidas por el servidor de base de datos sea superior al número máximo de procesos que atienden solicitudes web (más cualquier otro uso adicional, como tareas programadas o conexiones administrativas).

Consulta la documentación de tu base de datos para obtener información sobre cómo manejar conexiones abandonadas o inactivas (timeouts). Los timeouts largos pueden aumentar significativamente el número de conexiones persistentes abiertas en un momento dado.

## Posibles inconvenientes: Mantenimiento del estado de la conexión

Algunas extensiones de base de datos realizan limpieza automática al reutilizar la conexión; otras delegan esta tarea en el desarrollador de la aplicación. Según la extensión utilizada y el diseño de la aplicación, puede ser necesario realizar una limpieza manual antes de que el script finalice. Los cambios que pueden dejar la conexión en un estado inesperado incluyen:

Base de datos seleccionada o por defecto

Bloqueos de tablas

Transacciones no confirmadas

Tablas temporales

Configuraciones o características específicas de la conexión, como el perfilado

Los bloqueos de tablas y las transacciones que no se limpian ni cierran pueden provocar que otras consultas queden bloqueadas indefinidamente o que la reutilización posterior de la conexión genere cambios inesperados.

Tener seleccionada una base de datos incorrecta puede impedir que la conexión reutilizada ejecute las consultas como se espera (o que las ejecute sobre la base de datos equivocada si los esquemas son suficientemente similares).

Si no se eliminan las tablas temporales, las solicitudes posteriores no podrán recrear la misma tabla.

Puede implementar la limpieza utilizando destructores de clase o la función `register_shutdown_function`. También puede considerar el uso de proxies dedicados para agrupación de conexiones que incluyan esta funcionalidad.

## Palabras finales

Dado su comportamiento y los posibles inconvenientes descritos anteriormente, no debería utilizar conexiones persistentes sin una evaluación cuidadosa. No deben emplearse sin realizar cambios adicionales en su aplicación y sin una configuración meticulosa del servidor de base de datos, del servidor web y/o de PHP-FPM.

Considere soluciones alternativas, como investigar y corregir las causas del sobrecoste en la creación de conexiones (por ejemplo, desactivar las búsquedas inversas de DNS en el servidor de base de datos), o utilizar proxies dedicados para agrupación de conexiones.

Para APIs web de alto volumen, considere el uso de entornos de ejecución alternativos o servidores de aplicaciones de larga duración.

## Véase también

ibase_pconnect

oci_pconnect

odbc_pconnect

pfsockopen

pg_connect

Mysqli y conexiones persistentes

Gestor de conexiones PDO
