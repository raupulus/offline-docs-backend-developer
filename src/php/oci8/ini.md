---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/oci8.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 6047c10c1
order: 57700
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [oci8.connection_class](#ini.oci8.connection-class) | "" | `INI_ALL` |  |
| [oci8.default_prefetch](#ini.oci8.default-prefetch) | "100" | `INI_SYSTEM` |  |
| [oci8.events](#ini.oci8.events) | Off | `INI_SYSTEM` |  |
| [oci8.max_persistent](#ini.oci8.max-persistent) | "-1" | `INI_SYSTEM` |  |
| [oci8.old_oci_close_semantics](#ini.oci8.old-oci-close-semantics) | Off | `INI_SYSTEM` | Deprecado a partir de PHP 8.1.0. |
| [oci8.persistent_timeout](#ini.oci8.persistent-timeout) | "-1" | `INI_SYSTEM` |  |
| [oci8.ping_interval](#ini.oci8.ping-interval) | "60" | `INI_SYSTEM` |  |
| [oci8.prefetch_lob_size](#ini.oci8.prefetch-lob-size) | "0" | `INI_SYSTEM` | Disponible a partir de PECL OCI8 3.2. |
| [oci8.privileged_connect](#ini.oci8.privileged-connect) | Off | `INI_SYSTEM` |  |
| [oci8.statement_cache_size](#ini.oci8.statement-cache-size) | "20" | `INI_SYSTEM` |  |

Opciones de configuración OCI8

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`oci8.connection_class` `string`  
El texto definido por el usuario es utilizado por las conexiones del pool de conexiones residente de la base de datos Oracle 11*g* para particionar el pool. Esto permite a las conexiones persistentes OCI8 de una aplicación reutilizar las sesiones a la base de datos desde un script anterior, permitiendo así una mejor eficiencia. Cuando una aplicación utiliza un proceso de base de datos previamente utilizado con una clase de conexión diferente, las configuraciones de la sesión, como el formato de fecha por defecto de Oracle, serán reinicializadas. Este comportamiento permite evitar compartir accidentalmente información entre las diferentes aplicaciones.

El valor puede ser definido en tiempo de ejecución gracias a la función `ini_set`, llamada antes de la conexión.

Para utilizar DRCP, OCI8 debe estar vinculado con las bibliotecas Oracle 11*g* y la base de datos debe ser Oracle 11*g*. El pool de conexión debe estar activado en la base de datos, la opción de configuración `oci8.connection_class` debe valer la misma cadena para todos los servidores web utilizando la misma aplicación, y la cadena de conexión OCI8 debe especificar el uso de un servidor con pool.

`oci8.default_prefetch` `int`  
Esta opción define el número por defecto de líneas adicionales que serán recuperadas y almacenadas en caché automáticamente cada vez que se realice una consulta de bajo nivel recuperando datos desde la base de datos. Definir un valor de `0` permite desactivar esta funcionalidad.

El valor de pre-carga no altera el número de líneas que funciones como `oci_fetch_array` devolverán al usuario; la pre-carga y el almacenamiento en caché de líneas es gestionado internamente por OCI8.

El valor puede ser definido para cada consulta, ejecutando la función `oci_set_prefetch` antes de ejecutar la consulta.

Al utilizar Oracle 12*c* o posterior, el valor de pre-carga definido por PHP puede ser sobreescrito por el archivo de configuración del cliente Oracle: `oraaccess.xml`. Consulte la documentación de Oracle para más información.

> [!NOTE]
> Si se introduce un valor demasiado grande, esto puede conducir a una mejora de las prestaciones, a costa del uso de memoria. Para consultas que devuelven un gran número de datos, la ganancia de rendimiento puede ser realmente significativa.

`oci8.events` `bool`  
Definir esta opción a `On` permite a PHP ser notificado de los eventos de base de datos FAN (`Fast Application Notification`).

Sin FAN, cuando una instancia de la base de datos o un nodo de máquinas falla bruscamente, las aplicaciones PHP pueden bloquearse esperando una respuesta de la base de datos, hasta el final del tiempo de espera TCP. Con los eventos FAN, las aplicaciones PHP son notificadas rápidamente de los errores que afectan a las conexiones a la base de datos. La extensión OCI8 limpiará las conexiones inutilizables en la caché de conexiones persistentes.

Cuando se utiliza `On` como valor, la base de datos también debe estar configurada para emitir los eventos FAN.

El soporte de FAN está disponible cuando OCI8 está vinculado a bibliotecas Oracle 10*g*R2 (y posteriores) y conectado a una base de datos Oracle 10*g*R2 (y posteriores).

`oci8.max_persistent` `int`  
El número máximo de conexiones persistentes OCI8 por proceso PHP. Definir esta opción a -1 significa que no hay límite.

`oci8.old_oci_close_semantics` `bool`  
Esta opción controla el comportamiento de la función `oci_close`. Activar esta opción significa que `oci_close` no hará nada; la conexión no será cerrada hasta que finalice el script. Esto es únicamente para asegurar la compatibilidad ascendente. Si se piensa que es necesario activar esta opción, se *recomienda encarecidamente* eliminar las llamadas a la función `oci_close` de la aplicación en lugar de activar esta opción.

`oci8.persistent_timeout` `int`  
El tiempo máximo (en segundos) que un proceso PHP dado está autorizado a mantener una conexión persistente. Definir esta opción a -1 significa que las conexiones persistentes serán siempre mantenidas mientras el proceso PHP no termine o la conexión sea explícitamente cerrada usando la función `oci_close`.

> [!NOTE]
> En PHP, la expiración de los recursos persistentes no produce ninguna alerta. Ocurre cuando PHP termina un script y verifica el timestamp del último uso del recurso. Además, las conexiones persistentes solo pueden ser cerradas durante alguna actividad (no necesaria en OCI8) en el proceso PHP. Si hay más de un proceso PHP, entonces cada uno de ellos debe ser activado manualmente para iniciar la expiración de sus propios recursos. La introducción del pool de conexiones persistentes (DRCP) en Oracle 11*g* resuelve los problemas de memoria y recursos, que las opciones `oci8.max_persistent` y `oci8.persistent_timeout` intentaron resolver previamente.

`oci8.ping_interval` `int`  
El tiempo máximo (en segundos) a esperar antes de enviar un ping durante `oci_pconnect`. Cuando se define a 0, las conexiones persistentes serán verificadas en cada reutilización. Para desactivar completamente los pings, defina esta opción a -1.

> [!NOTE]
> Desactivar los pings hace que las llamadas a `oci_pconnect` sean altamente rentables, pero impide a PHP detectar problemas de conexión, como problemas de red, o si el servidor Oracle ha sido apagado desde la conexión de PHP, hasta que la conexión no sea utilizada más tarde en el script. Consulte la documentación de la función `oci_pconnect` para más información.

`oci8.prefetch_lob_size` `int`  
Se trata de un parámetro de ajuste que afecta al almacenamiento en memoria interna de los datos LOB. Aumentar este valor puede mejorar el rendimiento de recuperación de pequeños LOB reduciendo los intercambios entre PHP y la base de datos. El uso de la memoria cambiará.

El valor afecta a los LOB devueltos como instancias OCILob así como a aquellos devueltos usando `OCI_RETURN_LOBS`.

El valor puede ser definido por instrucción con `oci_set_prefetch_lob` antes de ejecutar la instrucción.

> [!NOTE]
> Para usar con Oracle Database 12.2 o posterior.

`oci8.privileged_connect` `bool`  
Esta opción activa las conexiones privilegiadas utilizando derechos externos (`OCI_SYSOPER`, `OCI_SYSDBA`).

> [!NOTE]
> Definir este valor a `On` permite a los scripts del servidor web ejecutando los privilegios de usuario del sistema apropiados conectarse a la base de datos utilizando estos privilegios, sin necesidad de proporcionar una contraseña a la base de datos. Esto puede tener consecuencias en términos de seguridad.

`oci8.statement_cache_size` `int`  
Esta opción activa la caché de consultas, y especifica el número de consultas a almacenar en caché. Para desactivar la caché de consultas, defina esta opción a 0.

La caché de consultas permite no tener que transmitir el texto de la consulta a la base de datos, así como no tener que transmitir metadatos sobre la consulta a PHP. Esto permite aumentar significativamente el rendimiento del sistema en las aplicaciones, reutilizando las consultas durante toda la vida de la conexión. Los "cursores" de base de datos también pueden ayudar si se parte de la base de que las consultas serán reutilizadas.

Defina este valor al tamaño de su conjunto de consultas comunes utilizadas por su aplicación. Definir un valor demasiado pequeño puede hacer que sus consultas sean eliminadas de la caché antes de que sean utilizadas.

Esta opción es más utilizada con las conexiones persistentes.

Con la base de datos Oracle 12*c*, este valor puede ser sobreescrito y ajustado automáticamente por el archivo `oraaccess.xml` del cliente Oracle. Consulte la documentación de Oracle para más explicaciones.
