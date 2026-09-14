---
title: sqlsrv_num_fields
description: Recupera el número de campos (columnas) en una consulta
source_url: https://www.php.net/manual/es/function.sqlsrv-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86250
---

sqlsrv_num_fields

Recupera el número de campos (columnas) en una consulta

## Descripción

```php
sqlsrv_num_fields(resource $stmt): mixed
```php

Recupera el número de campos (columnas) en una consulta.

## Parámetros

`stmt`  
La consulta desde la cual se devuelve el número de campos. La función `sqlsrv_num_fields` puede ser llamada sobre una consulta antes o después de la ejecución de la consulta.

## Valores devueltos

Devuelve el número de campos en caso de éxito. Devuelve `false` en caso contrario.

## Ejemplos

Ejemplo con `sqlsrv_num_fields`

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
   die( print_r( sqlsrv_errors(), true));
}

$sql = "SELECT * FROM Table_1";
$stmt = sqlsrv_query($conn, $sql);
if( $stmt === false) {
   die( print_r( sqlsrv_errors(), true));
}

$numFields = sqlsrv_num_fields( $stmt );

while( sqlsrv_fetch( $stmt )) {
   // Iteración sobre los campos de cada fila.
   for($i = 0; $i < $numFields; $i++) {
      echo sqlsrv_get_field($stmt, $i)." ";
   }
   echo "<br />";
}
?>

   
```php

## Véase también

sqlsrv_field_metadata

sqlsrv_fetch

sqlsrv_get_field
