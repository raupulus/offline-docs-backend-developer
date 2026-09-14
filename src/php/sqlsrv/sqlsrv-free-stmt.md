---
title: sqlsrv_free_stmt
description: Libera todos los recursos de la consulta especificada
source_url: https://www.php.net/manual/es/function.sqlsrv-free-stmt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-free-stmt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86200
---

sqlsrv_free_stmt

Libera todos los recursos de la consulta especificada

## Descripción

```php
sqlsrv_free_stmt(resource $stmt): bool
```php

Libera todos los recursos para la consulta especificada. La consulta no podrá ser utilizada después de pasar a la función `sqlsrv_free_stmt`. Si la función `sqlsrv_free_stmt` es llamada mientras la consulta está en ejecución, la ejecución de la consulta es interrumpida y la consulta es cancelada.

## Parámetros

`stmt`  
La consulta cuyos recursos serán liberados. Tenga en cuenta que `null` es un valor de argumento válido. Este valor permite que la función sea llamada varias veces en un script.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `sqlsrv_free_stmt`

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$stmt = sqlsrv_query( $conn, "SELECT * FROM Table_1");
if( $stmt === false ) {
     die( print_r( sqlsrv_errors(), true));
}

/*-------------------------------
     Uso de la consulta aquí.
-------------------------------*/

/* Liberación de los recursos asociados a la consulta. */
sqlsrv_free_stmt( $stmt);

?>

   
```php

## Notas

La principal diferencia entre la función `sqlsrv_free_stmt` y la función `sqlsrv_cancel` es que un recurso de consulta cancelado con la función `sqlsrv_cancel` puede ser re-ejecutado si ha sido creado con la función `sqlsrv_prepare`. Un recurso de consulta cancelado con la función `sqlsrv_free_statement` no puede ser re-ejecutado.

## Véase también

sqlsrv_cancel
