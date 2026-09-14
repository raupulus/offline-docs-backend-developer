---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mysqlnd.config.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/config.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 56120
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mysqlnd.collect_statistics](#ini.mysqlnd.collect-statistics) | "1" | `INI_SYSTEM` |  |
| [mysqlnd.collect_memory_statistics](#ini.mysqlnd.collect-memory-statistics) | "0" | `INI_SYSTEM` |  |
| [mysqlnd.debug](#ini.mysqlnd.debug) | "" | `INI_SYSTEM` |  |
| [mysqlnd.log_mask](#ini.mysqlnd.log-mask) | 0 | `INI_ALL` |  |
| [mysqlnd.mempool_default_size](#ini.mysqlnd.mempool-default-size) | 16000 | `INI_ALL` |  |
| [mysqlnd.net_read_timeout](#ini.mysqlnd.net-read-timeout) | "86400" | `INI_ALL` | Antes de PHP 7.2.0 el valor por omisión era "31536000" y la variabilidad era `INI_SYSTEM` |
| [mysqlnd.net_cmd_buffer_size](#ini.mysqlnd.net-cmd-buffer-size) | "4096" | `INI_SYSTEM` |  |
| [mysqlnd.net_read_buffer_size](#ini.mysqlnd.net-read-buffer-size) | "32768" | `INI_SYSTEM` |  |
| [mysqlnd.sha256_server_public_key](#ini.mysqlnd.sha256-server-public-key) | "" | `INI_PERDIR` |  |
| [mysqlnd.trace_alloc](#ini.mysqlnd.trace-alloc) | "" | `INI_SYSTEM` |  |
| [mysqlnd.fetch_data_copy](#ini.mysqlnd.fetch_data_copy) | 0 | `INI_ALL` | Eliminado a partir de PHP 8.1.0 |

Opciones de configuración de MySQL Native Driver {#mysqlnd.config.options}

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mysqlnd.collect_statistics` `bool`  
Activa la recolección de diferentes estadísticas del cliente a las cuales se puede acceder mediante `mysqli_get_client_stats`, `mysqli_get_connection_stats`, y que también se describen en la sección `mysqlnd` de la salida de la función `phpinfo`.

Este parámetro activa todas [ las estadísticas de MySQL Native Driver ](#mysqlnd.stats) excepto las relativas a la gestión de la memoria.

`mysqlnd.collect_memory_statistics` `bool`  
Activa la recolección de diferentes estadísticas concernientes a la memoria que pueden ser consultadas mediante `mysqli_get_client_stats`, `mysqli_get_connection_stats`, y que también se muestran en la sección `mysqlnd` de la salida de la función `phpinfo`.

Este parámetro activa las estadísticas de gestión de la memoria entre [las estadísticas proporcionadas por MySQL Native Driver](#mysqlnd.stats).

`mysqlnd.debug` `string`  
Registra las comunicaciones provenientes de cualquier extensión que utilice `mysqlnd`.

El formato de esta directiva es `mysqlnd.debug = "option1[,parameter_option1][:option2[,parameter_option2]]"`.

Las opciones de formato de strings son las siguientes:

- A\[,file\] - Añade la traza a un fichero. Asegura que los datos son escritos después de cada escritura cerrando y volviendo a abrir el fichero de traza (lento). Esto ayuda a asegurar que el fichero de trazas será completo incluso si la aplicación falla.

- a\[,file\] - Añade la traza a un fichero.

- d - Activa la salida desde las macros DBUG\_\<N\> para el estado actual. Puede ser seguido de una lista de palabras clave que seleccionan la salida solo para las macros DBUG con esa palabra clave (filtro). Una lista vacía de palabras clave seleccionará todo.

- f\[,functions\] - Limita las acciones del depurador a una lista específica de funciones. Una lista vacía hará que todas las funciones sean utilizadas.

- F - Marca cada línea de depuración con el nombre del fichero fuente que contiene la macro que causa esta salida.

- i - Marca cada línea de depuración con el PID.

- L - Marca cada línea de depuración con el nombre del fichero fuente así como la línea de la macro que causa esta salida.

- n - Marca cada línea de depuración con la profundidad actual de la función.

- o\[,file\] - Similar a a\[,file\] pero sobrescribe los ficheros en lugar de complementarlos.

- O\[,file\] - Similar a A\[,file\] pero sobrescribe los ficheros en lugar de complementarlos.

- t\[,N\] - Activa el trazado del flujo de control de las funciones. La profundidad máxima se especifica mediante N, por omisión 200.

- x - Activa el perfilado.

- m - Trazar las asignaciones y desasignaciones de memoria.

Ejemplo:

    d:t:x:O,/tmp/mysqlnd.trace

        

> [!NOTE]
> Esta característica solo está disponible para las versiones de depuración de PHP.

`mysqlnd.log_mask` `int`  
Define qué consulta será historizada. Por omisión, vale 0, lo que significa que los logs están desactivados. Conviene definir esta opción utilizando un entero, y no una constante PHP. Por ejemplo, un valor de 48 (16 + 32) historizará las consultas lentas que utilicen 'no good index' (SERVER_QUERY_NO_GOOD_INDEX_USED = 16) o ningún índice en absoluto (SERVER_QUERY_NO_INDEX_USED = 32). Un valor de 2043 (1 + 2 + 8 + ... + 1024) historizará todo tipo de consultas lentas.

Los tipos son los siguientes: SERVER_STATUS_IN_TRANS=1, SERVER_STATUS_AUTOCOMMIT=2, SERVER_MORE_RESULTS_EXISTS=8, SERVER_QUERY_NO_GOOD_INDEX_USED=16, SERVER_QUERY_NO_INDEX_USED=32, SERVER_STATUS_CURSOR_EXISTS=64, SERVER_STATUS_LAST_ROW_SENT=128, SERVER_STATUS_DB_DROPPED=256, SERVER_STATUS_NO_BACKSLASH_ESCAPES=512, y SERVER_QUERY_WAS_SLOW=1024.

`mysqlnd.mempool_default_size` `int`  
Tamaño por omisión de la cola de memoria mysqlnd, utilizada por los juegos de resultados.

`mysqlnd.net_read_timeout` `int`  
`mysqlnd` y la MySQL Client Library, `libmysqlclient` utilizan API de red diferentes. `mysqlnd` utiliza los flujos PHP, mientras que `libmysqlclient` utiliza su propia implementación basada en el sistema. PHP, por omisión, utiliza un timeout de lectura de 60s. Esto utilizando el parámetro de `php.ini`, `default_socket_timeout`. Esto se aplica a todos los flujos que no especifican un timeout por omisión. `mysqlnd` no afecta ningún otro valor y por lo tanto las consultas largas pueden verse desconectadas después de `default_socket_timeout` segundos con el resultado de un mensaje de error “2006 - MySQL Server has gone away”. La MySQL Client Library afecta un timeout por omisión de 24 \* 3600 segundos (1 día) y espera otros timeouts, como los de TCP/IP. `mysqlnd` utiliza ahora el mismo timeout muy largo. El valor es configurable mediante el parámetro `php.ini` `mysqlnd.net_read_timeout`. `mysqlnd.net_read_timeout` es por lo tanto utilizado por cualquier extensión (`ext/mysql`, `ext/mysqli`, `PDO_MySQL`) que se basa en `mysqlnd`. `mysqlnd` indica a los flujos PHP utilizar `mysqlnd.net_read_timeout`. Tenga en cuenta que puede haber diferencias sutiles entre `MYSQL_OPT_READ_TIMEOUT` de la MySQL Client Library y los flujos PHP, por ejemplo `MYSQL_OPT_READ_TIMEOUT` se dice funcional únicamente con conexiones TCP/IP y, antes de MySQL 5.1.2, solo en Windows. Los flujos PHP, ellos, no tienen esta limitación. Consulte la documentación de los flujos en caso de duda.

`mysqlnd.net_cmd_buffer_size` `int`  
`mysqlnd` asigna un buffer interno para la red de un tamaño de `mysqlnd.net_cmd_buffer_size` (en `php.ini`) bytes para cada conexión. Si una orden del protocolo MySQL Client Server, por ejemplo, `COM_QUERY` (consulta “normal”), no cabe en el buffer, `mysqlnd` aumentará aquel a la tamaño requerido. Cada vez que el buffer es aumentado para una conexión, `command_buffer_too_small` será incrementado en uno.

Si `mysqlnd` debe aumentar el buffer más allá de su tamaño inicial de `mysqlnd.net_cmd_buffer_size` bytes para casi todas las conexiones, entonces debería aumentar este tamaño por omisión para evitar las reasignaciones.

El tamaño por omisión del buffer es de 4096 bytes.

El valor también puede ser cambiado mediante `mysqli_options(link, MYSQLI_OPT_NET_CMD_BUFFER_SIZE, size)`.

`mysqlnd.net_read_buffer_size` `int`  
Tamaño máximo del segmento en lectura al leer el cuerpo de un paquete de orden MySQL. El protocolo servidor de MySQL encapsula todas sus órdenes en paquetes. Los paquetes consisten en un encabezado corto seguido de un cuerpo que contiene las informaciones. El tamaño del cuerpo está codificado en el encabezado. `mysqlnd` lee el cuerpo en forma de segmentos de `MIN(header.size, mysqlnd.net_read_buffer_size)` bytes. Si el cuerpo de un paquete es más grande que `mysqlnd.net_read_buffer_size` bytes, `mysqlnd` debe entonces llamar a `read()` varias veces.

El valor también puede ser cambiado mediante `mysqli_options(link, MYSQLI_OPT_NET_READ_BUFFER_SIZE, size)`.

`mysqlnd.sha256_server_public_key` `string`  
Relacionado con el plugin de autenticación SHA-256. Fichero que contiene la clave pública RSA en el servidor MySQL.

Los clientes pueden omitir definir una clave pública RSA y especificar la clave mediante la directiva de configuración PHP, o bien, definir la clave en el momento de la ejecución utilizando la función `mysqli_options`. Si ningún fichero de clave pública RSA es proporcionado por el cliente, entonces la clave será intercambiada conforme al procedimiento del plugin de autenticación estándar SHA-256.

`mysqlnd.trace_alloc` `string`  

`mysqlnd.fetch_data_copy` `int`  
Obliga a copiar los juegos de resultados desde los buffers internos hacia variables PHP en lugar de utilizar el mecanismo por omisión de referencia y copia al escribir. Consulte las, [notas de implementación sobre la gestión de memoria](#mysqlnd.memory) para más detalles.

Copiar los juegos de resultados en lugar de tener variables PHP que los referencian permite liberar más pronto la memoria ocupada por las variables PHP. Dependiendo del código de la API cliente, las consultas actuales y el tamaño de sus juegos de resultados, esto puede reducir la huella de memoria de mysqlnd.

No activar con PDO_MySQL. PDO_MySQL no soporta aún este modo.

> [!NOTE]
> Eliminado a partir de PHP 8.1.0
