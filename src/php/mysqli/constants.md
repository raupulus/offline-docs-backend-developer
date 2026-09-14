---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/mysqli.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 5208882ce
order: 54800
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`MYSQLI_READ_DEFAULT_GROUP` (`int`)  
Lee las opciones en el grupo `my.cnf` o en el archivo especificado por `MYSQLI_READ_DEFAULT_FILE`.

`MYSQLI_READ_DEFAULT_FILE` (`int`)  
Lee las opciones en el archivo especificado, en lugar de en `my.cnf`.

`MYSQLI_OPT_CAN_HANDLE_EXPIRED_PASSWORDS` (`int`)  
Indica al servidor que el cliente puede gestionar el modo sandbox para las contraseñas expiradas. Puede ser utilizado con `mysqli_options`.

`MYSQLI_OPT_LOAD_DATA_LOCAL_DIR` (`int`)  
Si está activada, esta opción especifica el directorio desde el cual la carga de datos `LOCAL` del lado del cliente está autorizada en las instrucciones `LOAD DATA LOCAL`.

`MYSQLI_OPT_CONNECT_TIMEOUT` (`int`)  
Tiempo de expiración de la conexión, en segundos.

`MYSQLI_OPT_READ_TIMEOUT` (`int`)  
Tiempo de expiración de la ejecución de un comando en segundos. Disponible a partir de PHP 7.2.0.

`MYSQLI_OPT_LOCAL_INFILE` (`int`)  
Activa el comando `LOAD LOCAL INFILE`.

`MYSQLI_OPT_INT_AND_FLOAT_NATIVE` (`int`)  
Convierte las columnas de tipo entero y número de coma flotante en números PHP. Solo válido para mysqlnd.

`MYSQLI_OPT_NET_CMD_BUFFER_SIZE` (`int`)  
El tamaño del buffer interno de comando/red. Solo válido para mysqlnd.

`MYSQLI_OPT_NET_READ_BUFFER_SIZE` (`int`)  
Tamaño en bytes de la porción máxima a leer, al leer el cuerpo de un paquete de comando MySQL. Solo válido para mysqlnd.

`MYSQLI_OPT_SSL_VERIFY_SERVER_CERT` (`int`)  

`MYSQLI_INIT_COMMAND` (`int`)  
Comando a ejecutar al conectarse al servidor MySQL. Este comando se ejecutará automáticamente al reconectarse al servidor.

`MYSQLI_CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS` (`int`)  
Indica al servidor que el cliente puede gestionar el modo sandbox para las contraseñas expiradas. Puede ser utilizado con `mysqli_real_connect`.

`MYSQLI_CLIENT_FOUND_ROWS` (`int`)  
Devuelve el número de filas coincidentes, no el número de filas afectadas.

`MYSQLI_CLIENT_SSL_VERIFY_SERVER_CERT` (`int`)  
Verifica el certificado del servidor.

`MYSQLI_CLIENT_SSL` (`int`)  
Utiliza el protocolo SSL (cifrado). Esta opción no debe ser activada por un programa: debe ser activada internamente, por la biblioteca MySQL.

`MYSQLI_CLIENT_COMPRESS` (`int`)  
Utiliza el protocolo comprimido.

`MYSQLI_CLIENT_INTERACTIVE` (`int`)  
Permite `interactive_timeout` segundos (en lugar de `wait_timeout` segundos) de inactividad antes de cerrar la conexión. El valor de la variable `wait_timeout` del cliente tomará el valor de `interactive_timeout`.

`MYSQLI_CLIENT_IGNORE_SPACE` (`int`)  
Permite espacios después de un nombre de función. Esto hace que todos los nombres de funciones sean palabras reservadas.

`MYSQLI_CLIENT_NO_SCHEMA` (`int`)  
Prohíbe la sintaxis `db_name.tbl_name.col_name`.

`MYSQLI_CLIENT_MULTI_QUERIES`  
Permite múltiples consultas separadas por un punto y coma en una sola llamada a la función `mysqli_query`.

`MYSQLI_STORE_RESULT` (`int`)  
Para los resultados almacenados en búfer. Tiene un valor de `0`.

`MYSQLI_STORE_RESULT_COPY_DATA` (`int`)  
Desde PHP 8.1, esta constante ya no tiene ningún efecto. Antes de PHP 8.1, esta constante se utilizaba para copiar los resultados del búfer interno `mysqlnd` en las variables PHP recuperadas. Por defecto, `mysqlnd` utilizará una lógica de referencia para evitar copiar y duplicar los resultados mantenidos en memoria. Para ciertos conjuntos de resultados, por ejemplo, conjuntos de resultados con muchas filas pequeñas, el enfoque de copia puede reducir el uso global de la memoria ya que las variables PHP que contienen los resultados pueden ser liberadas antes. Disponible únicamente con `mysqlnd`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_USE_RESULT` (`int`)  
Para los resultados no almacenados en búfer. Tiene un valor de `1`.

`MYSQLI_ASSOC` (`int`)  
Las columnas se devuelven en el array, con sus nombres como índices.

`MYSQLI_NUM` (`int`)  
Las columnas se devuelven en el array, con sus números como índices.

`MYSQLI_BOTH` (`int`)  
Las columnas se devuelven en el array, con sus nombres y sus números como índices.

`MYSQLI_NOT_NULL_FLAG` (`int`)  
Indica que un campo está definido como `NOT NULL`.

`MYSQLI_PRI_KEY_FLAG` (`int`)  
El campo es una clave primaria.

`MYSQLI_UNIQUE_KEY_FLAG` (`int`)  
El campo es un índice único.

`MYSQLI_MULTIPLE_KEY_FLAG` (`int`)  
El campo forma parte de un índice.

`MYSQLI_BLOB_FLAG` (`int`)  
El campo es de tipo `BLOB`.

`MYSQLI_UNSIGNED_FLAG` (`int`)  
El campo es de tipo `UNSIGNED`.

`MYSQLI_ZEROFILL_FLAG` (`int`)  
El campo es de tipo `ZEROFILL`.

`MYSQLI_AUTO_INCREMENT_FLAG` (`int`)  
El campo es de tipo `AUTO_INCREMENT`.

`MYSQLI_TIMESTAMP_FLAG` (`int`)  
El campo es de tipo `TIMESTAMP`.

`MYSQLI_SET_FLAG` (`int`)  
El campo es de tipo `SET`.

`MYSQLI_NUM_FLAG` (`int`)  
El campo es de tipo `NUMERIC`.

`MYSQLI_PART_KEY_FLAG` (`int`)  
El campo forma parte de un índice múltiple.

`MYSQLI_GROUP_FLAG` (`int`)  
El campo forma parte de la cláusula `GROUP BY`.

`MYSQLI_NO_DEFAULT_VALUE_FLAG` (`int`)  
Una columna no tiene una cláusula `DEFAULT` en su definición. Esto no se aplica a las columnas `NULL` o `AUTO_INCREMENT` ya que estas columnas tienen respectivamente un valor por defecto de `NULL` y un valor por defecto implícito.

`MYSQLI_TYPE_DECIMAL` (`int`)  
El campo es de tipo `DECIMAL`.

`MYSQLI_TYPE_NEWDECIMAL` (`int`)  
El campo es de tipo `DECIMAL` o `NUMERIC`.

`MYSQLI_TYPE_BIT` (`int`)  
El campo es de tipo `BIT`.

`MYSQLI_TYPE_TINY` (`int`)  
El campo es de tipo `TINYINT`.

`MYSQLI_TYPE_SHORT` (`int`)  
El campo es de tipo `SMALLINT`.

`MYSQLI_TYPE_LONG` (`int`)  
El campo es de tipo `INT`.

`MYSQLI_TYPE_FLOAT` (`int`)  
El campo es de tipo `FLOAT`.

`MYSQLI_TYPE_DOUBLE` (`int`)  
El campo es de tipo `DOUBLE`.

`MYSQLI_TYPE_NULL` (`int`)  
El campo es de tipo `DEFAULT NULL`.

`MYSQLI_TYPE_TIMESTAMP` (`int`)  
El campo es de tipo `TIMESTAMP`.

`MYSQLI_TYPE_LONGLONG` (`int`)  
El campo es de tipo `BIGINT`.

`MYSQLI_TYPE_INT24` (`int`)  
El campo es de tipo `MEDIUMINT`.

`MYSQLI_TYPE_DATE` (`int`)  
El campo es de tipo `DATE`.

`MYSQLI_TYPE_TIME` (`int`)  
El campo es de tipo `TIME`.

`MYSQLI_TYPE_DATETIME` (`int`)  
El campo es de tipo `DATETIME`.

`MYSQLI_TYPE_YEAR` (`int`)  
El campo es de tipo `YEAR`.

`MYSQLI_TYPE_NEWDATE` (`int`)  
El campo es de tipo `DATE`.

`MYSQLI_TYPE_INTERVAL` (`int`)  
Alias de `MYSQLI_TYPE_ENUM`. Eliminado desde PHP 8.4.0.

`MYSQLI_TYPE_ENUM` (`int`)  
El campo es de tipo `ENUM`.

`MYSQLI_TYPE_SET` (`int`)  
El campo es de tipo `SET`.

`MYSQLI_TYPE_TINY_BLOB` (`int`)  
El campo es de tipo `TINYBLOB`.

`MYSQLI_TYPE_MEDIUM_BLOB` (`int`)  
El campo es de tipo `MEDIUMBLOB`.

`MYSQLI_TYPE_LONG_BLOB` (`int`)  
El campo es de tipo `LONGBLOB`.

`MYSQLI_TYPE_BLOB` (`int`)  
El campo es de tipo `BLOB`.

`MYSQLI_TYPE_VAR_STRING` (`int`)  
El campo es de tipo `VARCHAR`.

`MYSQLI_TYPE_STRING` (`int`)  
El campo es de tipo `STRING` o `BINARY`.

`MYSQLI_TYPE_CHAR` (`int`)  
El campo es de tipo `TINYINT`. Para `CHAR`, ver `MYSQLI_TYPE_STRING`.

`MYSQLI_TYPE_GEOMETRY` (`int`)  
El campo es de tipo `GEOMETRY`.

`MYSQLI_TYPE_JSON` (`int`)  
El campo es de tipo `JSON`. Únicamente válido para mysqlnd y MySQL 5.7.8 y posteriores.

`MYSQLI_TYPE_VECTOR` (`int`)  
El campo está definido como `VECTOR`.

`MYSQLI_NEED_DATA`  
Quedan variables por enlazar.

`MYSQLI_ENUM_FLAG` (`int`)  
El campo está definido como `ENUM`.

`MYSQLI_BINARY_FLAG` (`int`)  
El campo está definido como `BINARY`.

`MYSQLI_CURSOR_TYPE_FOR_UPDATE` (`int`)  

`MYSQLI_CURSOR_TYPE_NO_CURSOR` (`int`)  
Eliminado a partir de PHP 8.4.0.

`MYSQLI_CURSOR_TYPE_READ_ONLY` (`int`)  
Eliminado a partir de PHP 8.4.0.

`MYSQLI_CURSOR_TYPE_SCROLLABLE` (`int`)  
Eliminado a partir de PHP 8.4.0.

`MYSQLI_STMT_ATTR_CURSOR_TYPE` (`int`)  

`MYSQLI_STMT_ATTR_PREFETCH_ROWS` (`int`)  

`MYSQLI_STMT_ATTR_UPDATE_MAX_LENGTH` (`int`)  

`MYSQLI_SET_CHARSET_NAME` (`int`)  

`MYSQLI_REPORT_INDEX` (`int`)  
Reporta si se utiliza un índice incorrecto o ningún índice en una consulta.

`MYSQLI_REPORT_ERROR` (`int`)  
Reporta los errores desde llamadas a funciones mysqli.

`MYSQLI_REPORT_STRICT` (`int`)  
Lanza una excepción `mysqli_sql_exception` para los errores en lugar de alertas.

`MYSQLI_REPORT_ALL` (`int`)  
Activa todas las opciones.

`MYSQLI_REPORT_OFF` (`int`)  
Desactiva todas las opciones.

`MYSQLI_DEBUG_TRACE_ENABLED` (`int`)  
Establecido en 1 si la funcionalidad `mysqli_debug` está desactivada.

`MYSQLI_SERVER_PUBLIC_KEY` (`int`)  

`MYSQLI_REFRESH_GRANT` (`int`)  
Refresca las tablas GRANT. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_LOG` (`int`)  
Vacía los logs, idéntico a ejecutar la consulta SQL `FLUSH LOGS`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_TABLES` (`int`)  
Vacía la caché de las tablas, idéntico a ejecutar la consulta SQL `FLUSH TABLES`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_HOSTS` (`int`)  
Vacía la caché de los hosts, idéntico a ejecutar la consulta SQL `FLUSH HOSTS`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_REPLICA` (`int`)  
Alias de la constante `MYSQLI_REFRESH_SLAVE`. Disponible a partir de PHP 8.1.0. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_STATUS` (`int`)  
Reinicia el estado de las variables, idéntico a ejecutar la consulta SQL `FLUSH STATUS`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_THREADS` (`int`)  
Vacía la caché de los hilos. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_SLAVE` (`int`)  
En un servidor esclavo de replicación: reinicia las informaciones del servidor maestro, y reinicia el esclavo. Idéntico a ejecutar la consulta SQL `RESET SLAVE`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_MASTER` (`int`)  
En un servidor maestro de replicación: elimina los archivos binarios de logs listados en el índice binario de logs, y trunca el archivo índice. Idéntico a ejecutar la consulta SQL `RESET MASTER`. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_REFRESH_BACKUP_LOG` (`int`)  
Cierra y reabre los archivos de registro de copia de seguridad. Obsoleto a partir de PHP 8.4.0.

`MYSQLI_TRANS_COR_AND_CHAIN` (`int`)  
Añade "AND CHAIN" a `mysqli_commit` o `mysqli_rollback`.

`MYSQLI_TRANS_COR_AND_NO_CHAIN` (`int`)  
Añade "AND NO CHAIN" a `mysqli_commit` o `mysqli_rollback`.

`MYSQLI_TRANS_COR_RELEASE` (`int`)  
Añade "RELEASE" a `mysqli_commit` o `mysqli_rollback`.

`MYSQLI_TRANS_COR_NO_RELEASE` (`int`)  
Añade "NO RELEASE" a `mysqli_commit` o `mysqli_rollback`.

`MYSQLI_TRANS_START_READ_ONLY` (`int`)  
Inicia la transacción como "START TRANSACTION READ ONLY".

`MYSQLI_TRANS_START_READ_WRITE` (`int`)  
Inicia la transacción como "START TRANSACTION READ WRITE" con `mysqli_begin_transaction`.

`MYSQLI_TRANS_START_WITH_CONSISTENT_SNAPSHOT` (`int`)  
Inicia la transacción como "START TRANSACTION WITH CONSISTENT SNAPSHOT" con `mysqli_begin_transaction`.

`MYSQLI_CLIENT_SSL_DONT_VERIFY_SERVER_CERT` (`int`)  
Requiere MySQL 5.6.5 o posterior.

`MYSQLI_IS_MARIADB` (`bool`)  
Si la extensión mysqli fue construida contra una biblioteca cliente MariaDB. Disponible a partir de PHP 8.1.2.

`MYSQLI_ASYNC` (`int`)  
La consulta se ejecuta de manera asíncrona y ningún conjunto de resultados es devuelto inmediatamente. Disponible únicamente con `mysqlnd`.

`MYSQLI_ON_UPDATE_NOW_FLAG` (`int`)  
Si un campo es actualizado, recibirá el valor temporal actual.
