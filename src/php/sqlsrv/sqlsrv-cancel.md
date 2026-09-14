---
title: sqlsrv_cancel
description: Cancela una sentencia de base de datos
source_url: https://www.php.net/manual/es/function.sqlsrv-cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86080
---

sqlsrv_cancel

Cancela una sentencia de base de datos

## Descripción

```php
sqlsrv_cancel(resource $stmt): bool
```php

Cancela una sentencia de base de datos. Cualquier resultado asociado con la sentencia que no haya sido utilizado será eliminado. Después de llamar a `sqlsrv_cancel` , la sentencia especificada puede ser reejecutada si fue creada con `sqlsrv_prepare`. No es necesario llamar a `sqlsrv_cancel` si todos los resultados asociados se han utilizado.

## Parámetros

`stmt`  
El recurso de la sentencia que se va a cancelar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `sqlsrv_cancel`

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT Sales FROM Table_1";

$stmt = sqlsrv_prepare( $conn, $sql);

if( $stmt === false ) {
     die( print_r( sqlsrv_errors(), true));
}

if( sqlsrv_execute( $stmt ) === false) {
     die( print_r( sqlsrv_errors(), true));
}

$salesTotal = 0;
$count = 0;

while( ($row = sqlsrv_fetch_array( $stmt)) && $salesTotal <=100000)
{
     $qty = $row[0];
     $price = $row[1];
     $salesTotal += ( $price * $qty);
     $count++;
}

echo "$count ventas suman los primeros $$salesTotal en ingresos.<br />";

// Cancela los resultados pendientes. La sentencia se puede reutilizar.
sqlsrv_cancel( $stmt);
?>

   
```php

## Notas

La principal diferencia entre `sqlsrv_cancel` y `sqlsrv_free_stmt` es que una sentencia cancelada con `sqlsrv_cancel` puede ser reejecutada si fue creada con `sqlsrv_prepare`. Una sentencia cancelada con `sqlsrv_free_statement` no puede ser reejecutada.

## Véase también

sqlsrv_free_stmt

sqlsrv_prepare
