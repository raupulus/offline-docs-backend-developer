---
title: sqlsrv_has_rows
description: Indica si la consulta especificada contiene filas
source_url: https://www.php.net/manual/es/function.sqlsrv-has-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-has-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86230
---

sqlsrv_has_rows

Indica si la consulta especificada contiene filas

## Descripción

```php
sqlsrv_has_rows(resource $stmt): bool
```php

Indica si la consulta especificada contiene filas.

## Parámetros

`stmt`  
Un recurso de consulta devuelto por la función `sqlsrv_query` o la función `sqlsrv_execute`.

## Valores devueltos

Devuelve `true` si la consulta especificada contiene filas, `false` si no contiene ninguna o si ocurre un error.

## Ejemplos

Ejemplo con `sqlsrv_has_rows`

```
<?php
$server = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password" );
$conn = sqlsrv_connect( $server, $connectionInfo );

$stmt = sqlsrv_query( $conn, "SELECT * FROM Table_1");

if ($stmt) {
   $rows = sqlsrv_has_rows( $stmt );
   if ($rows === true)
      echo "Hay filas. <br />";
   else
      echo "No hay filas. <br />";
}
?>

   
```php

## Véase también

sqlsrv_num_rows

sqlsrv_query
