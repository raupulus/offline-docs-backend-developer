---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pgsql.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: true
translation_revision: f5419b6ed
order: 62830
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`PGSQL_LIBPQ_VERSION` (`string`)  
Versión corta de libpq que solo contiene números y puntos.

`PGSQL_LIBPQ_VERSION_STR` (`string`)  
Anterior a PHP 8.0.0, la versión larga de libpq que incluye las informaciones del compilador. A partir de PHP 8.0.0, el valor es idéntico a `PGSQL_LIBPQ_VERSION`, y el uso de `PGSQL_LIBPQ_VERSION_STR` es obsoleto.

`PGSQL_ASSOC` (`int`)  
Pasada a `pg_fetch_array`. Devuelve un array asociativo de los nombres y valores de los campos.

`PGSQL_NUM` (`int`)  
Pasada a `pg_fetch_array`. Devuelve un array con índice numérico de los números y valores de los campos.

`PGSQL_BOTH` (`int`)  
Pasada a `pg_fetch_array`. Devuelve un array de los valores de los campos que está indexado numéricamente (por el número de los campos) y indexado literalmente (por el nombre de los campos).

`PGSQL_CONNECT_FORCE_NEW` (`int`)  
Pasada a `pg_connect` para forzar la creación de una nueva conexión, en lugar de reutilizar una conexión existente idéntica.

`PGSQL_CONNECT_ASYNC` (`int`)  
Pasada a la función `pg_connect` para crear una conexión asíncrona.

`PGSQL_CONNECTION_AUTH_OK` (`int`)  

`PGSQL_CONNECTION_AWAITING_RESPONSE` (`int`)  

`PGSQL_CONNECTION_BAD` (`int`)  
Retornada por `pg_connection_status` indicando que la conexión a la base de datos es inválida.

`PGSQL_CONNECTION_MADE` (`int`)  

`PGSQL_CONNECTION_OK` (`int`)  
Retornada por `pg_connection_status` indicando que la conexión a la base de datos es válida.

`PGSQL_CONNECTION_SETENV` (`int`)  

`PGSQL_CONNECTION_SSL_STARTUP` (`int`)  

`PGSQL_CONNECTION_STARTED` (`int`)  

`PGSQL_SEEK_SET` (`int`)  
Pasada a `pg_lo_seek`. El posicionamiento comenzará al inicio del objeto.

`PGSQL_SEEK_CUR` (`int`)  
Pasada a `pg_lo_seek`. El posicionamiento comenzará a la posición actual.

`PGSQL_SEEK_END` (`int`)  
Pasada a `pg_lo_seek`. El posicionamiento comenzará al final del objeto.

`PGSQL_EMPTY_QUERY` (`int`)  
Retornada por `pg_result_status`. La cadena de caracteres enviada al servidor estaba vacía.

`PGSQL_COMMAND_OK` (`int`)  
Retornada por `pg_result_status`. Comando correctamente completado sin devolver datos.

`PGSQL_TUPLES_OK` (`int`)  
Retornada por `pg_result_status`. Comando correctamente completado devolviendo datos (como `SELECT` o `SHOW`).

`PGSQL_TUPLES_CHUNK` (`int`)  
Retornado por `pg_result_status`. Indica el éxito en la ejecución de un comando que devuelve datos en modo por bloques. Retornado para los comandos `SELECT` cuando `pg_set_chunked_rows_size` está definido. El conjunto de resultados se divide en varios bloques, cada uno conteniendo un número predeterminado de filas. Disponible a partir de PHP 8.4.0 y libpq 17.

`PGSQL_COPY_OUT` (`int`)  
Retornada por `pg_result_status`. Copia (desde el servidor) de transferencia de datos iniciada.

`PGSQL_COPY_IN` (`int`)  
Retornada por `pg_result_status`. Copia (hacia el servidor) de transferencia de datos iniciada.

`PGSQL_BAD_RESPONSE` (`int`)  
Retornada por `pg_result_status`. La respuesta del servidor no ha sido comprendida.

`PGSQL_NONFATAL_ERROR` (`int`)  
Retornada por `pg_result_status`. Un error no fatal (de nivel notice o warning) ha ocurrido.

`PGSQL_FATAL_ERROR` (`int`)  
Retornada por `pg_result_status`. Un error fatal ha ocurrido.

`PGSQL_TRANSACTION_IDLE` (`int`)  
Retornada por `pg_transaction_Status`. La conexión está actualmente libre, sin transacción en curso.

`PGSQL_TRANSACTION_ACTIVE` (`int`)  
Retornada por `pg_transaction_status`. Un comando está en curso en la conexión. Una consulta ha sido enviada a la conexión y aún no ha sido completada.

`PGSQL_TRANSACTION_INTRANS` (`int`)  
Retornada por `pg_transaction_status`. La conexión está libre, dentro de un bloque de transacción.

`PGSQL_TRANSACTION_INERROR` (`int`)  
Retornada por `pg_transaction_status`. La conexión está libre, dentro de un bloque de transacción fallido.

`PGSQL_TRANSACTION_UNKNOWN` (`int`)  
Retornada por `pg_transaction_status`. La conexión es mala.

`PGSQL_DIAG_SEVERITY` (`int`)  
Pasada a `pg_result_error_field`. La severidad; el contenido del campo es `ERROR`, `FATAL` o `PANIC` (en un mensaje de error) o `WARNING`, `NOTICE`, `DEBUG`, `INFO` o `LOG` (en un mensaje de advertencia) o una traducción localizada de estos. Siempre presente.

`PGSQL_DIAG_SQLSTATE` (`int`)  
Pasada a `pg_result_error_field`. El código SQLSTATE para este error. El código SQLSTATE identifica el tipo de error que ha ocurrido; esto puede ser utilizado por aplicaciones de entrada para realizar operaciones específicas (como manejo de errores) en respuesta a un error particular de base de datos. Este campo no puede ser localizado y siempre está presente.

`PGSQL_DIAG_MESSAGE_PRIMARY` (`int`)  
Pasada a `pg_result_error_field`. El campo de error principal interpretable para el usuario (normalmente una línea). Siempre presente.

`PGSQL_DIAG_MESSAGE_DETAIL` (`int`)  
Pasada a `pg_result_error_field`. Detalle: un segundo mensaje de error opcional que aporta más detalles sobre el problema. Puede estar en varias líneas.

`PGSQL_DIAG_MESSAGE_HINT` (`int`)  
Pasada a `pg_result_error_field`. Consejo: una sugerencia opcional que indica qué hacer sobre el problema. Esto está previsto para ser diferente del error ya que ofrece un consejo (potencialmente inadecuado) en lugar de hechos verídicos. Puede estar en varias líneas.

`PGSQL_DIAG_STATEMENT_POSITION` (`int`)  
Pasada a `pg_result_error_field`. Una cadena de caracteres que contiene un valor entero decimal indicando una posición de error del cursor como índice en la consulta original. El primer carácter tiene el índice 1 y las posiciones son medidas en caracteres, no en bytes.

`PGSQL_DIAG_INTERNAL_POSITION` (`int`)  
Pasada a `pg_result_error_field`. Esto está definido siendo lo mismo que el campo `PG_DIAG_STATEMENT_POSITION`, pero esto se utiliza cuando la posición del cursor se refiere a una consulta generada internamente en lugar de una enviada por el cliente. El campo `PG_DIAG_INTERNAL_QUERY` aparecerá siempre cuando este campo aparezca.

`PGSQL_DIAG_INTERNAL_QUERY` (`int`)  
Pasada a `pg_result_error_field`. El texto de una consulta generada internamente fallida. Esto puede ser, por ejemplo, una consulta SQL enviada por una función PL/pgSQL.

`PGSQL_DIAG_CONTEXT` (`int`)  
Pasada a `pg_result_error_field`. Una indicación del contexto en el que el error ocurrió. Actualmente, esto incluye una pila de llamadas de traceback de las funciones procedimentales activas así como consultas generadas internamente. El rastreo es una entrada por línea, las más recientes primero.

`PGSQL_DIAG_SOURCE_FILE` (`int`)  
Pasada a `pg_result_error_field`. El nombre del archivo de la ubicación del código fuente de PostgreSQL donde el error fue reportado.

`PGSQL_DIAG_SOURCE_LINE` (`int`)  
Pasada a `pg_result_error_field`. El número de línea de la ubicación del código fuente de PostgreSQL donde el error fue reportado.

`PGSQL_DIAG_SOURCE_FUNCTION` (`int`)  
Pasada a `pg_result_error_field`. El nombre de la función del código fuente de PostgreSQL que reportó el error.

`PGSQL_DIAG_SCHEMA_NAME` (`int`)  
Disponible desde PHP 7.3.0.

`PGSQL_DIAG_TABLE_NAME` (`int`)  
Disponible desde PHP 7.3.0.

`PGSQL_DIAG_COLUMN_NAME` (`int`)  
Disponible desde PHP 7.3.0.

`PGSQL_DIAG_DATATYPE_NAME` (`int`)  
Disponible desde PHP 7.3.0.

`PGSQL_DIAG_CONSTRAINT_NAME` (`int`)  
Disponible desde PHP 7.3.0.

`PGSQL_ERRORS_TERSE` (`int`)  
Pasada a `pg_set_error_verbosity`. Especifica que los mensajes retornados incluyen la severidad, el texto principal así como la posición solamente; esto debería entrar en una sola línea.

`PGSQL_ERRORS_DEFAULT` (`int`)  
Pasada a `pg_set_error_verbosity`. El modo por omisión produce mensajes que incluyen lo anterior y detalles adicionales, consejos o campos de contexto (esto puede estar en varias líneas).

`PGSQL_ERRORS_VERBOSE` (`int`)  
Pasada a `pg_set_error_verbosity`. El modo verboso incluye todos los campos disponibles.

`PGSQL_ERRORS_SQLSTATE` (`int`)  
Pasado a `pg_set_error_verbosity`. Incluye únicamente la severidad del error y el código de error `SQLSTATE`. Si no hay código de error disponible, la salida es similar al modo `PGSQL_ERRORS_TERSE`. Antes de PostgreSQL 11.1, la salida es siempre la misma que en el modo `PGSQL_ERRORS_TERSE`.

`PGSQL_NOTICE_LAST` (`int`)  
Utilizado por `pg_last_notice`. Disponible a partir de PHP 7.1.0.

`PGSQL_NOTICE_ALL` (`int`)  
Utilizado por `pg_last_notice`. Disponible a partir de PHP 7.1.0.

`PGSQL_NOTICE_CLEAR` (`int`)  
Utilizado por `pg_last_notice`. Disponible a partir de PHP 7.1.0.

`PGSQL_STATUS_LONG` (`int`)  
Pasada a `pg_result_status`. Indica que el código de resultado es deseado numérico.

`PGSQL_STATUS_STRING` (`int`)  
Pasada a `pg_result_status`. Indica que la etiqueta de resultado de comando es deseada textual.

`PGSQL_CONV_IGNORE_DEFAULT` (`int`)  
Pasada a `pg_convert`. Ignora los valores por omisión en la tabla durante la conversión.

`PGSQL_CONV_FORCE_NULL` (`int`)  
Pasada a `pg_convert`. Utiliza SQL `null` en lugar de una `string` vacía.

`PGSQL_CONV_IGNORE_NOT_NULL` (`int`)  
Pasada a `pg_convert`. Ignora la conversión de `null` dentro de columnas `NOT NULL`.

`PGSQL_DML_NO_CONV` (`int`)  
Pasada a las funciones `pg_insert`, `pg_select`, `pg_update` y `pg_delete`. Todos los argumentos pasados tal cual. Un escape manual es necesario si los argumentos contienen datos proporcionados por el usuario. Utilice la función `pg_escape_string` para esto.

`PGSQL_DML_EXEC` (`int`)  
Pasada a las funciones `pg_insert`, `pg_select`, `pg_update` y `pg_delete`. Ejecución de la consulta por estas funciones.

`PGSQL_DML_ASYNC` (`int`)  
Pasada a las funciones `pg_insert`, `pg_select`, `pg_update` y `pg_delete`. Ejecución asíncrona de la consulta por estas funciones.

`PGSQL_DML_STRING` (`int`)  
Pasada a las funciones `pg_insert`, `pg_select`, `pg_update` y `pg_delete`. Devuelve la cadena de consulta ejecutada.

`PGSQL_DML_ESCAPE` (`int`)  
Pasada a las funciones `pg_insert`, `pg_select`, `pg_update` y `pg_delete`. Aplica un escape interno a todos los argumentos en lugar de llamar a la función `pg_convert`. Esta opción no maneja metadatos. La consulta debe ser tan rápida como con las funciones `pg_query` y `pg_send_query`.

`PGSQL_POLLING_FAILED` (`int`)  
Retornada por la función `pg_connect_poll` para indicar que el intento de conexión ha fallado.

`PGSQL_POLLING_READING` (`int`)  
Retornada por la función `pg_connect_poll` para indicar que la conexión está esperando a que el socket de PostgreSQL esté accesible en lectura.

`PGSQL_POLLING_WRITING` (`int`)  
Retornada por la función `pg_connect_poll` para indicar que la conexión está esperando a que el socket de PostgreSQL esté accesible en escritura.

`PGSQL_POLLING_OK` (`int`)  
Retornada por la función `pg_connect_poll` para indicar que la conexión está lista para ser utilizada.

`PGSQL_POLLING_ACTIVE` (`int`)  
Retornada por la función `pg_connect_poll` para indicar que la conexión está actualmente activa.

`PGSQL_DIAG_SEVERITY_NONLOCALIZED` (`int`)  
La severidad; los contenidos del campo son ERROR, FATAL, o PANIC (en un mensaje de error), o WARNING, NOTICE, DEBUG, INFO, o LOG (en un mensaje de aviso). Esto es idéntico al campo PG_DIAG_SEVERITY con la excepción de que los contenidos nunca son localizados. Esto está presente solo en las versiones 9.6 y posteriores / PHP 7.3.0 o superior.

`PGSQL_SHOW_CONTEXT_NEVER` (`int`)  
Para usar con `pg_set_error_context_visibility`, el contexto nunca es mostrado. Disponible a partir de PHP 8.3.0.

`PGSQL_SHOW_CONTEXT_ERRORS` (`int`)  
Para usar con `pg_set_error_context_visibility`, los campos del contexto son incluidos únicamente en los mensajes de error. Este es el comportamiento por omisión. Disponible a partir de PHP 8.3.0.

`PGSQL_SHOW_CONTEXT_ALWAYS` (`int`)  
Para usar con `pg_set_error_context_visibility`, los campos del contexto son incluidos en los mensajes de error, avisos y advertencias. Disponible a partir de PHP 8.3.0.

`PGSQL_TRACE_SUPPRESS_TIMESTAMPS` (`int`)  
Para usar con `pg_trace`, la marca de tiempo no es incluida en los mensajes de traza. Disponible a partir de PHP 8.4.20.

`PGSQL_TRACE_REGRESS_MODE` (`int`)  
Para usar con `pg_trace`, campos como los OIDs son incluidos en los mensajes de traza. Disponible a partir de PHP 8.3.0.
