---
title: sqlsrv_get_field
description: Recupera los datos del campo desde la línea actualmente seleccionada
source_url: https://www.php.net/manual/es/function.sqlsrv-get-field.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-get-field.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86220
---

sqlsrv_get_field

Recupera los datos del campo desde la línea actualmente seleccionada

## Descripción

```php
sqlsrv_get_field(resource $stmt, int $fieldIndex, [int $getAsType]): mixed
```php

Recupera los datos del campo desde la línea actualmente seleccionada. Los campos deben ser leídos en orden. Sus índices comienzan en 0.

## Parámetros

`stmt`  
Un recurso de consulta devuelto por la función `sqlsrv_query` o la función `sqlsrv_execute`.

`fieldIndex`  
El índice del campo a recuperar. Los índices de los campos comienzan en 0. Los campos deben ser leídos en orden, es decir, si se accede al campo con índice 1, el campo con índice 0 ya no estará disponible.

`getAsType`  
El tipo de datos PHP para los datos del campo devuelto. Si este argumento no está definido, los datos del campo serán devueltos en forma de un tipo de datos PHP por omisión. Para más información sobre los tipos de datos PHP por omisión, consulte la sección sobre [los tipos de datos PHP por omisión](http://msdn.microsoft.com/en-us/library/cc296193.aspx) de la documentación Microsoft SQLSRV.

## Valores devueltos

Devuelve los datos desde el campo especificado en caso de éxito. Devuelve `false` si ocurre un error.

## Ejemplos

`sqlsrv_get_field` example

El siguiente ejemplo muestra cómo recuperar una línea con la función `sqlsrv_fetch` y recupera los campos de la línea con la función `sqlsrv_get_field`.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT Name, Comment
        FROM Table_1
        WHERE ReviewID=1";
$stmt = sqlsrv_query( $conn, $sql);
if( $stmt === false ) {
     die( print_r( sqlsrv_errors(), true));
}

// Hace disponible la primera (y en este caso, la única) línea del conjunto de resultados para lectura.
if( sqlsrv_fetch( $stmt ) === false) {
     die( print_r( sqlsrv_errors(), true));
}

// Recupera los campos de la línea. Los índices comienzan en 0 y deben ser recuperados en orden.
// La recuperación de los campos de la línea por sus nombres no es soportada por la función sqlsrv_get_field.
$name = sqlsrv_get_field( $stmt, 0);
echo "$name: ";

$comment = sqlsrv_get_field( $stmt, 1);
echo $comment;
?>

   
```php

## Véase también

sqlsrv_fetch

sqlsrv_fetch_array

sqlsrv_fetch_object
