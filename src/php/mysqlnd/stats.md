---
title: Estadísticas
source_url: https://www.php.net/manual/es/mysqlnd.stats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/stats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: true
translation_revision: 9598935f2
order: 56200
---

## Estadísticas

El controlador nativo de MySQL contiene soporte para la recolección de estadísticas sobre la comunicación entre el cliente y el servidor. Las estadísticas recolectadas son de dos tipos principales:

- Estadísticas del cliente

- Estadísticas de la conexión

Cuando se utiliza la extensión [mysqli](#book.mysqli), estas estadísticas pueden obtenerse mediante dos llamadas API:

- `mysqli_get_client_stats`

- `mysqli_get_connection_stats`

> [!NOTE]
> Las estadísticas se agrupan entre todas las extensiones que utilizan el controlador nativo de MySQL. Por ejemplo, si la extensión [mysqli](#book.mysqli) y el controlador PDO MySQL están ambos configurados para usar MySQLnd, entonces las llamadas de funciones de [mysqli](#book.mysqli) y las llamadas de métodos de PDO afectarán las estadísticas.
>
> No hay manera de saber cuánto impacto ha tenido una cierta llamada API de una extensión que ha sido compilada sin el controlador nativo de MySQL en una cierta estadística.

## Recuperación de las estadísticas

Las estadísticas del cliente pueden recuperarse llamando a la función `mysqli_get_client_stats`.

Las estadísticas de conexión pueden recuperarse llamando a la función `mysqli_get_connection_stats`.

Las dos funciones devuelven un array asociativo, donde el nombre de una estadística es la clave para los datos estadísticos correspondientes.

## Estadísticas del controlador nativo de MySQL

La mayoría de las estadísticas están asociadas a una conexión, pero algunas están asociadas al proceso, en cuyo caso esto será mencionado.

Las siguientes estadísticas son producidas por el controlador nativo de MySQL:

`bytes_sent`  
El número de bytes enviados de PHP al servidor MySQL.

`bytes_received`  
El número de bytes recibidos del servidor MySQL.

`packets_sent`  
El número de paquetes enviados por el protocolo cliente-servidor MySQL.

`packets_received`  
El número de paquetes recibidos del protocolo cliente-servidor MySQL.

`protocol_overhead_in`  
La sobrecarga del protocolo cliente-servidor MySQL en bytes para el tráfico entrante. Actualmente, solo el encabezado de paquete (4 bytes) se considera como sobrecarga. `protocol_overhead_in = packets_received * 4`

`protocol_overhead_out`  
La sobrecarga del protocolo cliente-servidor MySQL en bytes para el tráfico saliente. Actualmente, solo el encabezado de paquete (4 bytes) se considera como sobrecarga. `protocol_overhead_out = packets_received * 4`

`bytes_received_ok_packet`  
El tamaño total en bytes de los paquetes OK del protocolo cliente-servidor MySQL recibidos. Los paquetes OK pueden contener un mensaje de estado. La longitud del mensaje de estado puede variar y por lo tanto el tamaño de un paquete OK no es fijo.

> [!NOTE]
> El tamaño total en bytes incluye el tamaño del encabezado del paquete (4 bytes, ver la sobrecarga del protocolo).

`packets_received_ok`  
El número de paquetes OK del protocolo cliente-servidor MySQL recibidos.

`bytes_received_eof_packet`  
El tamaño total en bytes de los paquetes EOF del protocolo cliente-servidor MySQL recibidos. El tamaño de un paquete EOF puede variar dependiendo de la versión del servidor. Además, un paquete EOF puede transportar un mensaje de error.

`packets_received_eof`  
El número de paquetes EOF del protocolo cliente-servidor MySQL recibidos.

Al igual que con otras estadísticas de paquetes, el número de paquetes será incrementado incluso si PHP no recibe el paquete esperado, sino, por ejemplo, un mensaje de error.

`bytes_received_rset_header_packet`  
El tamaño total en bytes de los encabezados de paquetes de resultados del protocolo cliente-servidor MySQL recibidos. El tamaño del encabezado del paquete puede variar dependiendo de la carga útil (`LOAD LOCAL INFILE`, `INSERT`, `UPDATE`, `SELECT`, mensaje de error).

`packets_received_rset_header`  
El número de paquetes de encabezados de resultados del protocolo cliente-servidor MySQL recibidos.

`bytes_received_rset_field_meta_packet`  
El tamaño total en bytes de los paquetes de metadatos de resultados del protocolo cliente-servidor (información de campo). Por supuesto, el tamaño varía con los campos del resultado. El paquete también puede transportar un error o un paquete EOF en caso de COM_LIST_FIELDS.

`packets_received_rset_field_meta`  
El número de paquetes de metadatos de resultados del protocolo cliente-servidor recibidos (información de campo).

`bytes_received_rset_row_packet`  
El tamaño total en bytes de los datos de fila de resultados del protocolo cliente-servidor MySQL recibidos. El paquete también puede transportar un error o un paquete EOF. Se puede calcular el número de errores y paquetes EOF restando `rows_fetched_from_server_normal` y `rows_fetched_from_server_ps` de `bytes_received_rset_row_packet`.

`packets_received_rset_row`  
El número de paquetes de datos de fila de resultados del protocolo cliente-servidor MySQL recibidos.

`bytes_received_prepare_response_packet`  
El tamaño total en bytes de los paquetes OK del protocolo cliente-servidor MySQL recibidos para la inicialización de declaraciones preparadas (paquetes de inicialización de declaración preparada). El paquete también puede transportar un error. El tamaño del paquete depende de la versión de MySQL.

`packets_received_prepare_response`  
El número de paquetes OK del protocolo cliente-servidor MySQL recibidos para la inicialización de declaraciones preparadas (paquetes de inicialización de declaración preparada).

`bytes_received_change_user_packet`  
El tamaño total en bytes de los paquetes COM_CHANGE_USER del protocolo cliente-servidor MySQL recibidos. El paquete también puede transportar un error o un paquete EOF.

`packets_received_change_user`  
El número de paquetes COM_CHANGE_USER del protocolo cliente-servidor MySQL recibidos.

`packets_sent_command`  
El número de comandos MySQL enviados por PHP al servidor MySQL.

No hay manera de saber qué comandos específicos y cuántos de ellos han sido enviados.

`bytes_received_real_data_normal`  
El número de bytes de carga útil recuperados por el cliente PHP desde `mysqlnd` usando el protocolo de texto.

Esto es el tamaño de los datos reales contenidos en los conjuntos de resultados que no provienen de declaraciones preparadas y que han sido recuperados por el cliente PHP.

Es de notar que aunque un conjunto de resultados completo haya podido ser extraído de MySQL por `mysqlnd`, esta estadística solo cuenta los datos reales extraídos de `mysqlnd` por el cliente PHP.

Un ejemplo de secuencia de código que incrementará el valor es el siguiente:

    $mysqli = new mysqli();
    $res = $mysqli->query("SELECT 'abc'");
    $res->fetch_assoc();
    $res->close();

          

Cada operación de recuperación incrementará el valor.

Sin embargo, la estadística no será incrementada si el conjunto de resultados es solo almacenado en búfer en el cliente, pero no extraído, como en el siguiente ejemplo:

    $mysqli = new mysqli();
    $res = $mysqli->query("SELECT 'abc'");
    $res->close();

          

`bytes_received_real_data_ps`  
El número de bytes de carga útil recuperados por el cliente PHP desde `mysqlnd` usando el protocolo de declaración preparada.

Esto es el tamaño de los datos reales contenidos en los conjuntos de resultados que provienen de declaraciones preparadas y que han sido recuperados por el cliente PHP.

El valor no será incrementado si el conjunto de resultados no es leído por el cliente PHP.

Es de notar que aunque un conjunto de resultados completo haya podido ser extraído de MySQL por `mysqlnd`, esta estadística solo cuenta los datos reales extraídos de `mysqlnd` por el cliente PHP.

Ver también `bytes_received_real_data_normal`.

<!-- -->

`result_set_queries`  
El número de consultas que han generado un conjunto de resultados. Ejemplos de consultas que generan un conjunto de resultados: `SELECT`, `SHOW`.

La estadística no será incrementada si hay un error al leer el encabezado del paquete del conjunto de resultados.

> [!NOTE]
> Esta estadística puede ser utilizada como medida indirecta del número de Esto puede ayudar a identificar un cliente que provoca una carga alta en la base de datos. consultas que PHP ha enviado a MySQL.

`non_result_set_queries`  
El número de consultas que no han generado un conjunto de resultados. Ejemplos de consultas que no generan un conjunto de resultados: `INSERT`, `UPDATE`, `LOAD DATA`.

Esta estadística no será incrementada si hay un error al leer el encabezado del paquete del conjunto de resultados.

`no_index_used`  
El número de consultas que han generado un conjunto de resultados pero no han utilizado un índice. (Ver también la opción de inicio de mysqld `--log-queries-not-using-indexes`).

> [!NOTE]
> Estas consultas pueden ser reportadas mediante una excepción llamando `mysqli_report(MYSQLI_REPORT_INDEX);`. Es posible reportarlas mediante un aviso llamando `mysqli_report(MYSQLI_REPORT_INDEX ^ MYSQLI_REPORT_STRICT);`.

`bad_index_used`  
El número de consultas que han generado un conjunto de resultados y no han utilizado un buen índice. (Ver también la opción de inicio de mysqld `--log-slow-queries`).

`slow_queries`  
Las declaraciones SQL que han tomado más de `long_query_time` segundos para ejecutarse y han necesitado al menos `min_examined_row_limit` filas para examinar.

> [!CAUTION]
> No reportado mediante `mysqli_report`.

`buffered_sets`  
El número de conjuntos de resultados almacenados en búfer devueltos por consultas normales (es decir, no mediante una declaración preparada).

Ejemplos de llamadas API que almacenarán en búfer los conjuntos de resultados en el cliente: `mysqli_query`, `mysqli_store_result`, `mysqli_stmt_get_result`

`unbuffered_sets`  
El número de conjuntos de resultados no almacenados en búfer devueltos por consultas normales (es decir, no mediante una declaración preparada).

Ejemplos de llamadas API que no almacenarán en búfer los conjuntos de resultados en el cliente: `mysqli_use_result`

`ps_buffered_sets`  
El número de conjuntos de resultados almacenados en búfer devueltos por declaraciones preparadas.

Ejemplos de llamadas API que almacenarán en búfer los conjuntos de resultados en el cliente: `mysqli_stmt_store_result`

`ps_unbuffered_sets`  
El número de conjuntos de resultados no almacenados en búfer devueltos por declaraciones preparadas.

Por omisión, las declaraciones preparadas no son almacenadas en búfer, por lo que la mayoría de las declaraciones preparadas serán contabilizadas en esta estadística.

`flushed_normal_sets`  
El número de juegos de resultados devueltos por consultas normales (es decir, no mediante una declaración preparada) con datos no leídos que han sido silenciosamente vaciados.

> [!NOTE]
> El vaciado solo ocurre con conjuntos de resultados no almacenados en búfer.
>
> Los conjuntos de resultados no almacenados en búfer deben ser recuperados completamente antes de que una nueva consulta pueda ser ejecutada en la conexión, de lo contrario MySQL lanzará un error. Si la aplicación no recupera todas las filas de un conjunto de resultados no almacenado en búfer, mysqlnd recupera implícitamente el conjunto de resultados para vaciar la fila.
>
> Ver también `rows_skipped_normal`, `rows_skipped_ps`.
>
> Algunas causas posibles para un vaciado implícito:
>
> - Aplicación cliente defectuosa
>
> - Cliente se detuvo de leer después de encontrar lo que buscaba pero hizo que MySQL calculara más filas de las necesarias
>
> - La aplicación cliente se detuvo de manera inesperada

`flushed_ps_sets`  
El número de juegos de resultados devueltos por declaraciones preparadas con datos no leídos que han sido silenciosamente vaciados.

`ps_prepared_never_executed`  
El número de declaraciones preparadas preparadas pero nunca ejecutadas.

`ps_prepared_once_executed`  
El número de declaraciones preparadas ejecutadas una sola vez.

`rows_fetched_from_server_normal`; `rows_fetched_from_server_ps`  
El número total de filas de conjunto de resultados recuperadas del servidor. Esto incluye las filas que no han sido leídas por el cliente pero han sido recuperadas implícitamente debido a conjuntos de resultados no almacenados en búfer vaciados.

Ver también `packets_received_rset_row`.

`rows_buffered_from_client_normal`  
El número total de filas almacenadas en búfer provenientes de una consulta normal.

Esto es el número de filas que han sido recuperadas de MySQL y almacenadas en búfer en el cliente.

Ejemplos de consultas que almacenarán en búfer los conjuntos de resultados: `mysqli_query`, `mysqli_store_result`

`rows_buffered_from_client_ps`  
Equivalente a `rows_buffered_from_client_normal` pero para las declaraciones preparadas.

`rows_fetched_from_client_normal_buffered`  
El número total de filas recuperadas por el cliente desde un conjunto de resultados almacenado en búfer creado por una consulta normal.

`rows_fetched_from_client_ps_buffered`  
El número total de filas recuperadas por el cliente desde un conjunto de resultados almacenado en búfer creado por una declaración preparada.

`rows_fetched_from_client_normal_unbuffered`  
El número total de filas recuperadas por el cliente desde un conjunto de resultados no almacenado en búfer creado por una consulta normal.

`rows_fetched_from_client_ps_unbuffered`  
El número total de filas recuperadas por el cliente desde un conjunto de resultados no almacenado en búfer creado por una declaración preparada.

`rows_fetched_from_client_ps_cursor`  
El número total de filas recuperadas por el cliente desde un cursor creado por una declaración preparada.

`rows_skipped_normal`; `rows_skipped_ps`  
Reservado para uso futuro (actualmente no soportado).

`copy_on_write_saved`; `copy_on_write_performed`  
Esto es una estadística de alcance de proceso.

Con mysqlnd, las variables devueltas por las extensiones apuntan a mysqlnd búferes de resultados internos. Si los datos no son modificados, los datos extraídos solo se conservan una vez en memoria. Sin embargo, cualquier modificación de los datos requerirá que mysqlnd realice una operación de copia-al-escribir.

`explicit_free_result`; `implicit_free_result`  
Esto es una estadística de alcance de conexión y de proceso.

El número total de resultados liberados.

`proto_text_fetched_null`  
El número total de columnas de tipo `MYSQL_TYPE_NULL` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_null`  
El número total de columnas de tipo `MYSQL_TYPE_NULL` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_bit`  
El número total de columnas de tipo `MYSQL_TYPE_BIT` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_bit`  
El número total de columnas de tipo `MYSQL_TYPE_BIT` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_tinyint`  
El número total de columnas de tipo `MYSQL_TYPE_TINY` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_tinyint`  
El número total de columnas de tipo `MYSQL_TYPE_TINY` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_short`  
El número total de columnas de tipo `MYSQL_TYPE_SHORT` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_short`  
El número total de columnas de tipo `MYSQL_TYPE_SHORT` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_int24`  
El número total de columnas de tipo `MYSQL_TYPE_INT24` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_int24`  
El número total de columnas de tipo `MYSQL_TYPE_INT24` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_int`  
El número total de columnas de tipo `MYSQL_TYPE_LONG` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_int`  
El número total de columnas de tipo `MYSQL_TYPE_LONG` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_bigint`  
El número total de columnas de tipo `MYSQL_TYPE_LONGLONG` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_bigint`  
El número total de columnas de tipo `MYSQL_TYPE_LONGLONG` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_decimal`  
El número total de columnas de tipo `MYSQL_TYPE_DECIMAL`, o `MYSQL_TYPE_NEWDECIMAL` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_decimal`  
El número total de columnas de tipo `MYSQL_TYPE_DECIMAL`, o `MYSQL_TYPE_NEWDECIMAL` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_float`  
El número total de columnas de tipo `MYSQL_TYPE_FLOAT` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_float`  
El número total de columnas de tipo `MYSQL_TYPE_FLOAT` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_double`  
El número total de columnas de tipo `MYSQL_TYPE_DOUBLE` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_double`  
El número total de columnas de tipo `MYSQL_TYPE_DOUBLE` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_date`  
El número total de columnas de tipo `MYSQL_TYPE_DATE`, o `MYSQL_TYPE_NEWDATE` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_date`  
El número total de columnas de tipo `MYSQL_TYPE_DATE`, o `MYSQL_TYPE_NEWDATE` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_year`  
El número total de columnas de tipo `MYSQL_TYPE_YEAR` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_year`  
El número total de columnas de tipo `MYSQL_TYPE_YEAR` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_time`  
El número total de columnas de tipo `MYSQL_TYPE_TIME` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_time`  
El número total de columnas de tipo `MYSQL_TYPE_TIME` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_datetime`  
El número total de columnas de tipo `MYSQL_TYPE_DATETIME` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_datetime`  
El número total de columnas de tipo `MYSQL_TYPE_DATETIME` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_timestamp`  
El número total de columnas de tipo `MYSQL_TYPE_TIMESTAMP` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_timestamp`  
El número total de columnas de tipo `MYSQL_TYPE_TIMESTAMP` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_string`  
El número total de columnas de tipo `MYSQL_TYPE_STRING`, `MYSQL_TYPE_VARSTRING` o `MYSQL_TYPE_VARCHAR` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_string`  
El número total de columnas de tipo `MYSQL_TYPE_STRING`, `MYSQL_TYPE_VARSTRING` o `MYSQL_TYPE_VARCHAR` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_blob`  
El número total de columnas de tipo `MYSQL_TYPE_TINY_BLOB`, `MYSQL_TYPE_MEDIUM_BLOB`, `MYSQL_TYPE_LONG_BLOB`, o `MYSQL_TYPE_BLOB` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_blob`  
El número total de columnas de tipo `MYSQL_TYPE_TINY_BLOB`, `MYSQL_TYPE_MEDIUM_BLOB`, `MYSQL_TYPE_LONG_BLOB`, o `MYSQL_TYPE_BLOB` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_enum`  
El número total de columnas de tipo `MYSQL_TYPE_ENUM` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_enum`  
El número total de columnas de tipo `MYSQL_TYPE_ENUM` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_set`  
El número total de columnas de tipo `MYSQL_TYPE_SET` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_set`  
El número total de columnas de tipo `MYSQL_TYPE_SET` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_geometry`  
El número total de columnas de tipo `MYSQL_TYPE_GEOMETRY` recuperadas desde una consulta normal (protocolo de texto MySQL).

`proto_binary_fetched_geometry`  
El número total de columnas de tipo `MYSQL_TYPE_GEOMETRY` recuperadas desde una declaración preparada (protocolo binario MySQL).

`proto_text_fetched_other`  
El número total de columnas de tipos `MYSQL_TYPE_*` no listados anteriormente recuperadas desde una consulta normal (protocolo de texto MySQL).

> [!NOTE]
> En teoría, esto debería ser siempre `0`.

`proto_binary_fetched_other`  
El número total de columnas de tipo `MYSQL_TYPE_*` no listados anteriormente recuperadas desde una declaración preparada (protocolo binario MySQL).

> [!NOTE]
> En teoría, esto debería ser siempre `0`.

<!-- -->

`connect_success`  
El número total de intentos de conexión exitosos.

> [!NOTE]
> `connect_success` contiene la suma de los intentos de conexión persistentes y no persistentes exitosos. Por lo tanto, el número de intentos de conexión no persistentes exitosos es `connect_success - pconnect_success`.

`pconnect_success`  
El número total de intentos de conexión persistentes exitosos.

`connect_failure`  
El número total de intentos de conexión fallidos.

`reconnect`  
Esto es una estadística de alcance de proceso.

`active_connections`  
Esto es una estadística de alcance de proceso.

El número total de conexiones persistentes y no persistentes activas.

> [!NOTE]
> El número total de conexiones no persistentes activas es `active_connections - active_persistent_connections`.

`active_persistent_connections`  
Esto es una estadística de alcance de proceso.

El número total de conexiones persistentes activas.

`explicit_close`  
El número total de conexiones cerradas explícitamente.

Ejemplos de fragmentos de código que provocan un cierre explícito

-     $link = new mysqli(/* ... */);
      $link->close(/* ... */);

              

-     $link = new mysqli(/* ... */);
      $link->connect(/* ... */);

`implicit_close`  
El número total de conexiones cerradas implícitamente.

Ejemplos de fragmentos de código que provocan un cierre implícito

-     $link = new mysqli(/* ... */);
      $link->real_connect(/* ... */);

              

-              unset($link)
              

- Conexión persistente: una conexión agrupada ha sido creada con real_connect y puede haber opciones desconocidas definidas - cerrar implícitamente para evitar devolver una conexión con opciones desconocidas

- Conexión persistente: ping/change_user falla y ext/mysqli cierra la conexión

- Fin de la ejecución del script: cerrar conexiones que no han sido cerradas por el usuario

`disconnect_close`  
Fallos de conexión indicados por la llamada de API C `mysql_real_connect` durante un intento de establecer una conexión.

`in_middle_of_command_close`  
Esto es una estadística de alcance de proceso.

Una conexión ha sido cerrada en medio de la ejecución de un comando (conjuntos de resultados no recuperados, después de enviar una consulta y antes de recuperar una respuesta, durante la recuperación de datos, durante la transferencia de datos con LOAD DATA).

> [!WARNING]
> A menos que se usen consultas asíncronas, esto solo debería ocurrir si la aplicación PHP terminó inesperadamente y PHP cierra automáticamente la conexión.

`init_command_executed_count`  
El número total de ejecuciones de comandos de inicialización. Por ejemplo: `mysqli_options(MYSQLI_INIT_COMMAND , $value)`.

El número de ejecuciones exitosas es `init_command_executed_count - init_command_failed_count`.

`init_command_failed_count`  
El número total de fallos en la ejecución de comandos de inicialización.

<!-- -->

`com_quit`; `com_init_db`; `com_query`; `com_field_list`; `com_create_db`; `com_drop_db`; `com_refresh`; `com_shutdown`; `com_statistics`; `com_process_info`; `com_connect`; `com_process_kill`; `com_debug`; `com_ping`; `com_time`; `com_delayed_insert`; `com_change_user`; `com_binlog_dump`; `com_table_dump`; `com_connect_out`; `com_register_slave`; `com_stmt_prepare`; `com_stmt_execute`; `com_stmt_send_long_data`; `com_stmt_close`; `com_stmt_reset`; `com_stmt_set_option`; `com_stmt_fetch`; `com_daemon`  
El número total de intentos de enviar un cierto comando `COM_*` de PHP a MySQL.

La estadística es incrementada después de verificar la línea y justo antes de enviar el paquete de protocolo cliente-servidor MySQL correspondiente.

> [!CAUTION]
> Si MySQLnd falla al enviar el paquete en la red, las estadísticas no serán decrementadas. En caso de fallo, MySQLnd emite un aviso PHP “Error while sending %s packet. PID=%d.”

Ejemplos de uso

- Verificar si PHP envía ciertos comandos a MySQL, por ejemplo, verificar si un cliente envía `COM_PROCESS_KILL`

- Calcular el número promedio de ejecuciones de comandos preparados comparando `COM_EXECUTE` con `COM_PREPARE`

- Verificar si PHP ha ejecutado declaraciones SQL no preparadas verificando si `COM_QUERY` es cero

- Identificar los scripts PHP que ejecutan un número excesivo de declaraciones SQL verificando `COM_QUERY` y `COM_EXECUTE`

<!-- -->

`explicit_stmt_close`; `implicit_stmt_close`  
Esto es una estadística de alcance de proceso.

El número total de declaraciones preparadas cerradas explícitamente.

> [!NOTE]
> Una declaración preparada siempre es cerrada explícitamente. La única vez que es cerrada implícitamente es cuando su preparación falla.

`mem_emalloc_count`; `mem_emalloc_ammount`; `mem_ecalloc_count`; `mem_ecalloc_ammount`; `mem_realloc_count`; `mem_realloc_ammount`; `mem_efree_count`; `mem_malloc_count`; `mem_malloc_ammount`; `mem_calloc_count`; `mem_calloc_ammount`; `mem_ealloc_count`; `mem_ealloc_ammount`; `mem_free_count`  
Esto es una estadística de alcance de proceso.

Llamadas a la gestión de memoria.

`command_buffer_too_small`  
El número de extensiones de búfer de comando de red al enviar comandos de PHP a MySQL.

MySQLnd asigna un búfer de comando/red interno de [mysqlnd.net_cmd_buffer_size](#ini.mysqlnd.net-cmd-buffer-size) bytes para cada conexión.

Si un protocolo de comando de servidor MySQL, por ejemplo `COM_QUERY` (consulta normal), no cabe en el búfer, MyQSLnd extenderá el búfer a lo que sea necesario para enviar el comando. Cada vez que el búfer es extendido para una conexión `command_buffer_too_small` será incrementado en uno.

Si mysql es obligado a hacer crecer el búfer más allá de su tamaño inicial de [mysqlnd.net_cmd_buffer_size](#ini.mysqlnd.net-cmd-buffer-size) bytes para casi cada conexión, se deberían considerar aumentar el tamaño por defecto para evitar las reasignaciones.

`connection_reused`  
El número total de veces que una conexión persistente ha sido reutilizada.
