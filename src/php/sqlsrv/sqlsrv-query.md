---
title: sqlsrv_query
description: Prepara y ejecuta una consulta
source_url: https://www.php.net/manual/es/function.sqlsrv-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86280
---

sqlsrv_query

Prepara y ejecuta una consulta

## Descripción

```php
sqlsrv_query(resource $conn, string $sql, [array $params], [array $options]): mixed
```php

Prepara y ejecuta una consulta.

## Parámetros

`conn`  
Un recurso de conexión devuelto por la función `sqlsrv_connect`.

`sql`  
El string que define la consulta a preparar y ejecutar.

`params`  
Un array especificando los parámetros al ejecutar una consulta que los permita. Los elementos del array pueden ser cualquiera de los siguientes: Un valor literal, Una variable PHP, Un array con esta estructura: array(\$value \[, \$direction \[, \$phpType \[, \$sqlType\]\]\]) La tabla siguiente describe los elementos en la estructura del array anterior:

| Elemento | Descripción |
|----|----|
| \$value | Un valor literal, una variable PHP o una variable PHP por referencia. |
| \$direction (opcional) | Una de las constantes SQLSRV siguientes utilizadas para indicar la dirección del parámetro: SQLSRV_PARAM_IN, SQLSRV_PARAM_OUT, SQLSRV_PARAM_INOUT. El valor por defecto es SQLSRV_PARAM_IN. |
| \$phpType (opcional) | Una constante SQLSRV_PHPTYPE\_\* que especifica el tipo de datos PHP del valor devuelto. |
| \$sqlType (opcional) | Una constante SQLSRV_SQLTYPE\_\* que especifica el tipo de datos del servidor SQL para el valor de entrada. |

Estructura del array

`options`  
Un array especificando las opciones de la consulta. Las claves soportadas son descritas en la tabla siguiente:

| Clave | Valor | Descripción |
|----|----|----|
| QueryTimeout | Un valor entero positivo. | Define el tiempo máximo de ejecución de la consulta en segundos. Por defecto, el controlador esperará indefinidamente los resultados. |
| SendStreamParamsAtExec | `true` o `false` (por defecto, vale `true`) | Configura el controlador para enviar todos los flujos de datos a la ejecución (`true`) o enviar los flujos de datos en fragmentos (`false`). Para más información, ver la función `sqlsrv_send_stream_data`. |
| Scrollable | SQLSRV_CURSOR_FORWARD, SQLSRV_CURSOR_STATIC, SQLSRV_CURSOR_DYNAMIC, o SQLSRV_CURSOR_KEYSET | Ver el capítulo sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx) en la documentación Microsoft SQLSRV. |

Opciones de consulta

## Valores devueltos

Devuelve un recurso de consulta en caso de éxito, y `false` si ocurre un error.

## Ejemplos

`sqlsrv_query` ejemplo

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password" );
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$sql = "INSERT INTO Table_1 (id, data) VALUES (?, ?)";
$params = array(1, "some data");

$stmt = sqlsrv_query( $conn, $sql, $params);
if( $stmt === false ) {
     die( print_r( sqlsrv_errors(), true));
}
?>

   
```php

## Notas

Para las consultas que no se prevé ejecutar más de una vez, utilice la función `sqlsrv_query`. Si se desea re-ejecutar una consulta con diferentes valores para sus parámetros, utilice la combinación de la función `sqlsrv_prepare` y la función `sqlsrv_execute`.

## Véase también

sqlsrv_prepare

sqlsrv_execute
