---
title: sqlsrv_fetch
description: Hace que esté disponible para ser leída la siguiente fila del conjunto
  de resultado
source_url: https://www.php.net/manual/es/function.sqlsrv-fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86180
---

sqlsrv_fetch

Hace que esté disponible para ser leída la siguiente fila del conjunto de resultado

## Descripción

```php
sqlsrv_fetch(resource $stmt, [int $row], [int $offset]): mixed
```php

Hace que esté disponible para ser leída la siguiente fila del conjunto de resultado. Utilizar `sqlsrv_get_field` para leer los campos de la fila.

## Parámetros

`stmt`  
Un recurso de consulta creado por la ejecución de `sqlsrv_query` o `sqlsrv_execute`.

`row`  
La fila que será accedida. Este parámetro puede utilizarse si la consulta especificada se preparó con un cursor con scroll. En ese caso, el parámetro puede tomar uno de los siguientes valores: SQLSRV_SCROLL_NEXT, SQLSRV_SCROLL_PRIOR, SQLSRV_SCROLL_FIRST, SQLSRV_SCROLL_LAST, SQLSRV_SCROLL_ABSOLUTE, SQLSRV_SCROLL_RELATIVE

`offset`  
Especifica la fila que será accedida si el parámetro de fila se configura como `SQLSRV_SCROLL_ABSOLUTE` o `SQLSRV_SCROLL_RELATIVE`. Notar que la primera fila en el conjunto resultado tiene el índice 0.

## Valores devueltos

Devuelve `true` si la fila siguiente del conjunto de resultado se obtuvo satisfactoriamente, `false` si se produce un error, y `null` si no hay más filas en el conjunto de resultado.

## Ejemplos

Ejemplo con `sqlsrv_fetch`

El ejemplo siguiente demuestra como obtener una fila con `sqlsrv_fetch` y los campos de la fila con `sqlsrv_get_field`.

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

// Hacer que sea disponible para su lectura la primera (y en este caso única) fila del conjunto resultado.
if( sqlsrv_fetch( $stmt ) === false) {
     die( print_r( sqlsrv_errors(), true));
}

// Obtener los campos de la fila. Los índices de campo empiezan desde 0 y se deben obtener en orden.
// Recuperar los nombres de campo por su nombre no está soportado por sqlsrv_get_field.
$name = sqlsrv_get_field( $stmt, 0);
echo "$name: ";

$comment = sqlsrv_get_field( $stmt, 1);
echo $comment;
?>

   
```php

## Véase también

sqlsrv_get_field

sqlsrv_fetch_array

sqlsrv_fetch_object
