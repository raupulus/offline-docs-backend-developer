---
title: Resumen de las funciones de la extensión MySQLi
source_url: https://www.php.net/manual/es/mysqli.summary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/summary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 4e8c90ca8
order: 56090
---

## Resumen de las funciones de la extensión MySQLi

| Clase mysqli |  |  |  |
|----|----|----|----|
| Interfaz POO | Interfaz procedural | Alias (No usar más) | Descripción |
| **Propiedades** |  |  |  |
| [\$mysqli::affected_rows](#mysqli.affected-rows) | `mysqli_affected_rows` | N/A | Devuelve el número de filas afectadas por la última operación MySQL |
| [\$mysqli::client_info](#mysqli.get-client-info) | `mysqli_get_client_info` | N/A | Devuelve la versión del cliente MySQL en forma de `string` |
| [\$mysqli::client_version](#mysqli.get-client-version) | `mysqli_get_client_version` | N/A | Devuelve la información sobre la versión del cliente MySQL en forma de un entero |
| [\$mysqli::connect_errno](#mysqli.connect-errno) | `mysqli_connect_errno` | N/A | Devuelve el código de error de la conexión MySQL |
| [\$mysqli::connect_error](#mysqli.connect-error) | `mysqli_connect_error` | N/A | Devuelve el mensaje de error de la conexión MySQL |
| [\$mysqli::errno](#mysqli.errno) | `mysqli_errno` | N/A | Devuelve el código de error de conexión MySQL |
| [\$mysqli::error](#mysqli.error) | `mysqli_error` | N/A | Devuelve el mensaje de error de conexión MySQL |
| [\$mysqli::field_count](#mysqli.field-count) | `mysqli_field_count` | N/A | Devuelve el número de columnas para la última consulta |
| [\$mysqli::host_info](#mysqli.get-host-info) | `mysqli_get_host_info` | N/A | Devuelve una cadena que contiene el tipo de conexión utilizada |
| [\$mysqli::protocol_version](#mysqli.get-proto-info) | `mysqli_get_proto_info` | N/A | Devuelve la versión del protocolo MySQL utilizado |
| [\$mysqli::server_info](#mysqli.get-server-info) | `mysqli_get_server_info` | N/A | Devuelve un entero que representa la versión del servidor MySQL |
| [\$mysqli::server_version](#mysqli.get-server-version) | `mysqli_get_server_version` | N/A | Devuelve la versión del servidor MySQL |
| [\$mysqli::info](#mysqli.info) | `mysqli_info` | N/A | Devuelve información sobre la última consulta ejecutada |
| [\$mysqli::insert_id](#mysqli.insert-id) | `mysqli_insert_id` | N/A | Devuelve el identificador generado automáticamente por la última consulta |
| [\$mysqli::sqlstate](#mysqli.sqlstate) | `mysqli_sqlstate` | N/A | Devuelve el error SQLSTATE de la última operación MySQL |
| [\$mysqli::warning_count](#mysqli.warning-count) | `mysqli_warning_count` | N/A | Devuelve el número de advertencias generadas por la última consulta |
| **Métodos** |  |  |  |
| mysqli::autocommit | `mysqli_autocommit` | N/A | Activa o desactiva el modo auto-commit |
| mysqli::change_user | `mysqli_change_user` | N/A | Cambia el usuario de la conexión especificada |
| mysqli::character_set_name | `mysqli_character_set_name` | `N/A` | Devuelve el juego de caracteres actual para la conexión |
| mysqli::close | `mysqli_close` | N/A | Cierra una conexión |
| mysqli::commit | `mysqli_commit` | N/A | Valida la transacción actual |
| mysqli::\_\_construct | `mysqli_connect` | N/A | Abre una conexión a un servidor MySQL |
| mysqli::debug | `mysqli_debug` | N/A | Realiza acciones de depuración |
| mysqli::dump_debug_info | `mysqli_dump_debug_info` | N/A | Escribe la información de depuración en los registros |
| mysqli::get_charset | `mysqli_get_charset` | N/A | Devuelve un objeto que representa el juego de caracteres |
| mysqli::get_connection_stats | `mysqli_get_connection_stats` | N/A | Devuelve estadísticas sobre la conexión del cliente. Disponible solo con [mysqlnd](#book.mysqlnd). |
| mysqli::get_client_info | `mysqli_get_client_info` | N/A | Devuelve una cadena que contiene la versión del cliente MySQL |
| N/A | `mysqli_get_client_stats` | N/A | Devuelve las estadísticas del cliente MySQL. Disponible solo con [mysqlnd](#book.mysqlnd). |
| mysqli::get_server_info | `mysqli_get_server_info` | N/A | Devuelve una cadena que representa la versión del servidor MySQL al que la extensión MySQLi está conectada |
| mysqli::get_warnings | `mysqli_get_warnings` | N/A | No documentado |
| mysqli::init | `mysqli_init` | N/A | Inicializa MySQLi y devuelve un objeto para usar con mysqli_real_connect() |
| mysqli::kill | `mysqli_kill` | N/A | Solicita al servidor que termine un hilo MySQL |
| mysqli::more_results | `mysqli_more_results` | N/A | Verifica si hay más conjuntos de resultados MySQL disponibles |
| mysqli::multi_query | `mysqli_multi_query` | N/A | Ejecuta una consulta múltiple MySQL |
| mysqli::next_result | `mysqli_next_result` | N/A | Prepara el siguiente resultado de una consulta múltiple |
| mysqli::options | `mysqli_options` | `mysqli_set_opt` | Define las opciones |
| mysqli::ping | `mysqli_ping` | N/A | Hace ping a la conexión al servidor y se reconecta si ya no existe |
| mysqli::prepare | `mysqli_prepare` | N/A | Prepara una consulta SQL para su ejecución |
| mysqli::query | `mysqli_query` | N/A | Ejecuta una consulta en la base de datos |
| mysqli::real_connect | `mysqli_real_connect` | N/A | Abre una conexión a un servidor MySQL |
| mysqli::real_escape_string, mysqli::escape_string | `mysqli_real_escape_string` | `mysqli_escape_string` | Protege los caracteres especiales de una cadena para usarla en una consulta |
| mysqli::real_query | `mysqli_real_query` | N/A | Ejecuta una consulta SQL |
| mysqli::refresh | `mysqli_refresh` | N/A | Reinicializa las tablas o las cachés, o reinicializa la información de replicación del servidor |
| mysqli::rollback | `mysqli_rollback` | N/A | Revierte la transacción actual |
| mysqli::select_db | `mysqli_select_db` | N/A | Selecciona una base de datos por defecto para las consultas |
| mysqli::set_charset | `mysqli_set_charset` | N/A | Define el juego de caracteres por defecto del cliente |
| mysqli::ssl_set | `mysqli_ssl_set` | N/A | Utilizada para establecer una conexión segura con SSL |
| mysqli::stat | `mysqli_stat` | N/A | Obtiene el estado actual del sistema |
| mysqli::stmt_init | `mysqli_stmt_init` | N/A | Inicializa un comando MySQL |
| mysqli::store_result | `mysqli_store_result` | N/A | Transfiere un conjunto de resultados desde la última consulta |
| mysqli::thread_id | `mysqli_thread_id` | N/A | Devuelve el identificador del hilo para la conexión actual |
| mysqli::thread_safe | `mysqli_thread_safe` | N/A | Indica si el soporte de hilos está activado o no |
| mysqli::use_result | `mysqli_use_result` | N/A | Inicializa la recuperación de un conjunto de resultados |

Resumen de los métodos `mysqli` {#mysqli.summary.classtable}

| MySQL_STMT |  |  |  |
|----|----|----|----|
| Interfaz POO | Interfaz procedural | Alias (No usar más) | Descripción |
| **Propiedades** |  |  |  |
| [\$mysqli_stmt::affected_rows](#mysqli-stmt.affected-rows) | `mysqli_stmt_affected_rows` | N/A | El número total de filas modificadas, eliminadas o insertadas por la última |
| [\$mysqli_stmt::errno](#mysqli-stmt.errno) | `mysqli_stmt_errno` | N/A | El código de error de la última consulta |
| [\$mysqli_stmt::error](#mysqli-stmt.error) | `mysqli_stmt_error` | N/A | El mensaje de error de la última consulta |
| [\$mysqli_stmt::field_count](#mysqli-stmt.field-count) | `mysqli_stmt_field_count` | N/A | El número de campos presente en la consulta dada |
| [\$mysqli_stmt::insert_id](#mysqli-stmt.insert-id) | `mysqli_stmt_insert_id` | N/A | El ID generado por la última consulta INSERT |
| [\$mysqli_stmt::num_rows](#mysqli-stmt.num-rows) | `mysqli_stmt_num_rows` | N/A | El número de filas de un resultado MySQL |
| [\$mysqli_stmt::param_count](#mysqli-stmt.param-count) | `mysqli_stmt_param_count` | N/A | El número de parámetros de un comando SQL |
| [\$mysqli_stmt::sqlstate](#mysqli-stmt.sqlstate) | `mysqli_stmt_sqlstate` | N/A | El código SQLSTATE de la última operación MySQL |
| **Métodos** |  |  |  |
| mysqli_stmt::attr_get | `mysqli_stmt_attr_get` | N/A | Recupera el valor actual de un atributo de consulta |
| mysqli_stmt::attr_set | `mysqli_stmt_attr_set` | N/A | Modifica el comportamiento de una consulta preparada |
| mysqli_stmt::bind_param | `mysqli_stmt_bind_param` | N/A | Vincula variables a una consulta MySQL |
| mysqli_stmt::bind_result | `mysqli_stmt_bind_result` | N/A | Vincula variables a un conjunto de resultados |
| mysqli_stmt::close | `mysqli_stmt_close` | N/A | Termina una consulta preparada |
| mysqli_stmt::data_seek | `mysqli_stmt_data_seek` | N/A | Mueve el puntero de resultado |
| mysqli_stmt::execute | `mysqli_stmt_execute` | `mysqli_execute` | Ejecuta una consulta preparada |
| mysqli_stmt::fetch | `mysqli_stmt_fetch` | N/A | Lee resultados desde una consulta MySQL preparada en variables vinculadas |
| mysqli_stmt::free_result | `mysqli_stmt_free_result` | N/A | Libera el resultado MySQL de la memoria |
| mysqli_stmt::get_result | `mysqli_stmt_get_result` | N/A | Recupera el conjunto de resultados desde una consulta preparada. Disponible solo con [mysqlnd](#book.mysqlnd). |
| mysqli_stmt::get_warnings | `mysqli_stmt_get_warnings` | N/A | No documentado |
| mysqli_stmt::more_results | `mysqli_stmt_more_results` | N/A | Verifica si hay más resultados de consulta desde una consulta múltiple |
| mysqli_stmt::next_result | `mysqli_stmt_next_result` | N/A | Lee el siguiente resultado desde una consulta múltiple |
| mysqli_stmt::num_rows | `mysqli_stmt_num_rows` | N/A | Ver también la propiedad [\$mysqli_stmt-\>num_rows](#mysqli-stmt.num-rows) |
| mysqli_stmt::prepare | `mysqli_stmt_prepare` | N/A | Prepara una consulta SQL para su ejecución |
| mysqli_stmt::reset | `mysqli_stmt_reset` | N/A | Anula una consulta preparada |
| mysqli_stmt::result_metadata | `mysqli_stmt_result_metadata` | N/A | Devuelve los metadatos de preparación de consulta MySQL |
| mysqli_stmt::send_long_data | `mysqli_stmt_send_long_data` | N/A | Envía datos MySQL por paquetes |
| mysqli_stmt::store_result | `mysqli_stmt_store_result` | N/A | Almacena un conjunto de resultados desde una consulta preparada |

Resumen de los métodos `mysqli_stmt` {#mysqli.summary.methods}

| mysqli_result |  |  |  |
|----|----|----|----|
| Interfaz POO | Interfaz procedural | Alias (No usar más) | Descripción |
| **Propiedades** |  |  |  |
| [\$mysqli_result::current_field](#mysqli-result.current-field) | `mysqli_field_tell` | N/A | La posición actual de un campo en un puntero de resultado |
| [\$mysqli_result::field_count](#mysqli-result.field-count) | `mysqli_num_fields` | N/A | El número de campos en un resultado |
| [\$mysqli_result::lengths](#mysqli-result.lengths) | `mysqli_fetch_lengths` | N/A | Los tamaños de los campos en un resultado |
| [\$mysqli_result::num_rows](#mysqli-result.num-rows) | `mysqli_num_rows` | N/A | El número de filas en un resultado |
| **Métodos** |  |  |  |
| mysqli_result::data_seek | `mysqli_data_seek` | N/A | Mueve el puntero interno de resultado |
| mysqli_result::fetch_all | `mysqli_fetch_all` | N/A | Lee todas las filas de resultados en un array asociativo, numérico, o ambos. Disponible solo con [mysqlnd](#book.mysqlnd). |
| mysqli_result::fetch_array | `mysqli_fetch_array` | N/A | Devuelve una fila de resultado en forma de un array asociativo, un array indexado, o ambos |
| mysqli_result::fetch_assoc | `mysqli_fetch_assoc` | N/A | Recupera una fila de resultado en forma de array asociativo |
| mysqli_result::fetch_column | `mysqli_fetch_column` | N/A | Recupera una sola columna de la siguiente fila de un conjunto de resultados |
| mysqli_result::fetch_field_direct | `mysqli_fetch_field_direct` | N/A | Recupera los metadatos de un campo único |
| mysqli_result::fetch_field | `mysqli_fetch_field` | N/A | Devuelve el siguiente campo en el conjunto de resultados |
| mysqli_result::fetch_fields | `mysqli_fetch_fields` | N/A | Devuelve un array de objetos que representan los campos en el resultado |
| mysqli_result::fetch_object | `mysqli_fetch_object` | N/A | Devuelve la fila actual de un conjunto de resultados en forma de objeto |
| mysqli_result::fetch_row | `mysqli_fetch_row` | N/A | Recupera una fila de resultado en forma de array indexado |
| mysqli_result::field_seek | `mysqli_field_seek` | N/A | Mueve el puntero de resultado al campo especificado |
| mysqli_result::free, [mysqli_result::close](#mysqli-result.free), [mysqli_result::free_result](#mysqli-result.free) | `mysqli_free_result` | N/A | Libera la memoria asociada a un resultado |

Resumen de los métodos `mysqli_result` {#mysqli.summary.resultmethods}

| MySQL_Driver |  |  |  |
|----|----|----|----|
| Interfaz POO | Interfaz procedural | Alias (No usar más) | Descripción |
| **Propiedades** |  |  |  |
| [\$mysqli_driver::mysqli_report](#mysqli-driver.report-mode) | `mysqli_report` | N/A | Define el modo del informe de errores de mysqli |
| **Métodos** |  |  |  |
| mysqli_driver::embedded_server_end | `mysqli_embedded_server_end` | N/A | No documentado |
| mysqli_driver::embedded_server_start | `mysqli_embedded_server_start` | N/A | No documentado |

Resumen de los métodos `mysqli_driver` {#mysqli.summary.drivermethods}

> [!NOTE]
> Los alias se proporcionan para asegurar la compatibilidad ascendente. No se deben usar en nuevos proyectos.
