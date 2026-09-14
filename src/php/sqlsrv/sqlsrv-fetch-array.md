---
title: sqlsrv_fetch_array
description: Devuelve una fila como un array
source_url: https://www.php.net/manual/es/function.sqlsrv-fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86160
---

sqlsrv_fetch_array

Devuelve una fila como un array

## Descripción

```php
sqlsrv_fetch_array(resource $stmt, [int $fetchType], [int $row], [int $offset]): array
```php

Devuelve la siguiente fila de datos disponible como un array asociativo, un array numérico, o ambos (por defecto).

## Parámetros

`stmt`  
Un recurso de sentencia devuelta por sqlsrv_query o sqlsrv_prepare.

`fetchType`  
Una constante predefinida con el tipo de array a devolver. Los valores posibles son `SQLSRV_FETCH_ASSOC`, `SQLSRV_FETCH_NUMERIC`, y `SQLSRV_FETCH_BOTH` (por defecto).

El tipo de objeto devuelto SQLSRV_FETCH_ASSOC no debe utilizarse cuando se trate un conjunto de resultados con múltiples columnas con el mismo nombre.

`row`  
Especifica la fila para acceder a un conjunto de resultados que utiliza un cursor con scroll. Los valores posibles son `SQLSRV_SCROLL_NEXT`, `SQLSRV_SCROLL_PRIOR`, `SQLSRV_SCROLL_FIRST`, `SQLSRV_SCROLL_LAST`, `SQLSRV_SCROLL_ABSOLUTE` y, `SQLSRV_SCROLL_RELATIVE` (por defecto). Cuando se especifica este parámetro, el parámetro `fetchType` debe ser definido explícitamente.

`offset`  
Especifica la fila a la que se desea acceder si el parámetro de fila se define como `SQLSRV_SCROLL_ABSOLUTE` o `SQLSRV_SCROLL_RELATIVE`. Notar que la primera fila en un conjunto de resultado tiene el índice 0.

## Valores devueltos

Devuelve un array en caso de éxito, `null` si no hay más filas a devolver, y `false` si se produce un error.

## Ejemplos

Devolver un array asociativo.

```
<?php
$serverName = "serverName\instanceName";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo );
if( $conn === false ) {
    die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT FirstName, LastName FROM SomeTable";
$stmt = sqlsrv_query( $conn, $sql );
if( $stmt === false) {
    die( print_r( sqlsrv_errors(), true) );
}

while( $row = sqlsrv_fetch_array( $stmt, SQLSRV_FETCH_ASSOC) ) {
      echo $row['LastName'].", ".$row['FirstName']."<br />";
}

sqlsrv_free_stmt( $stmt);
?>

   
```php

Devolver un array numérico.

```
<?php
$serverName = "serverName\instanceName";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo );
if( $conn === false ) {
    die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT FirstName, LastName FROM SomeTable";
$stmt = sqlsrv_query( $conn, $sql );
if( $stmt === false) {
    die( print_r( sqlsrv_errors(), true) );
}

while( $row = sqlsrv_fetch_array( $stmt, SQLSRV_FETCH_NUMERIC) ) {
      echo $row[0].", ".$row[1]."<br />";
}

sqlsrv_free_stmt( $stmt);
?>

   
```php

## Notas

Cuando no se especifica el parámetro `fetchType` o se utiliza explícitamente la constante `SQLSRV_FETCH_TYPE` en los ejemplos anteriores, se devolverá un array que tiene tanto claves asociativas como claves nuéricas.

Si se devuelve más de una columna con el mismo nombre, la última columna tendrá prioridad para tomar el nombre. Para evitar colisiones de nombre de campo, utilizar alias.

Si se devuelve una columna sin nombre, la clave asociativa para ese elemento del array será un string vacío ("").

## Véase también

sqlsrv_connect

sqlsrv_query

sqlsrv_errors

sqlsrv_fetch
