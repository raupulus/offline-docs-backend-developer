---
title: sqlsrv_rows_affected
description: Devuelve el número de filas modificadas por la última consulta de tipo
  INSERT, UPDATE, o DELETE
source_url: https://www.php.net/manual/es/function.sqlsrv-rows-affected.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-rows-affected.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86300
---

sqlsrv_rows_affected

Devuelve el número de filas modificadas por la última consulta de tipo INSERT, UPDATE, o DELETE

## Descripción

```php
sqlsrv_rows_affected(resource $stmt): int
```php

Devuelve el número de filas modificadas por la última consulta de tipo INSERT, UPDATE, o DELETE. Para más información sobre el número de filas devueltas por una consulta SELECT, consulte la función `sqlsrv_num_rows`.

## Parámetros

`stmt`  
El recurso de la consulta ejecutada.

## Valores devueltos

Devuelve el número de filas afectadas por la última consulta INSERT, UPDATE, o DELETE. Si ninguna fila es afectada, se devolverá 0. Si el número de filas afectadas no puede ser determinado, se devolverá -1. Si ocurre un error, se devolverá `false`.

## Ejemplos

Ejemplo con `sqlsrv_rows_affected`

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password" );
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$sql = "UPDATE Table_1 SET data = ? WHERE id = ?";

$params = array("updated data", 1);

$stmt = sqlsrv_query( $conn, $sql, $params);

$rows_affected = sqlsrv_rows_affected( $stmt);
if( $rows_affected === false) {
     die( print_r( sqlsrv_errors(), true));
} elseif( $rows_affected == -1) {
      echo "No hay información disponible.<br />";
} else {
      echo $rows_affected." filas han sido actualizadas.<br />";
}
?>

   
```php

## Véase también

sqlsrv_num_rows
