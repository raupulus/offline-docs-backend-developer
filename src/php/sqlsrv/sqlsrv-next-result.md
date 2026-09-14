---
title: sqlsrv_next_result
description: Activa el siguiente resultado de la consulta especificada
source_url: https://www.php.net/manual/es/function.sqlsrv-next-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-next-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86240
---

sqlsrv_next_result

Activa el siguiente resultado de la consulta especificada

## Descripción

```php
sqlsrv_next_result(resource $stmt): mixed
```php

Activa el siguiente resultado de la consulta especificada. Los resultados incluyen los conjuntos de resultados, el número de filas y los parámetros de salida.

## Parámetros

`stmt`  
La consulta sobre la cual se llamará el siguiente resultado.

## Valores devueltos

Devuelve `true` si el siguiente resultado ha sido recuperado con éxito, `false` si ocurre un error, y `null` si no hay más resultados para recuperar.

## Ejemplos

Ejemplo con `sqlsrv_next_result`

El siguiente ejemplo ejecuta una consulta batch que realiza inserciones en una tabla y luego realiza una selección de la tabla. Esto produce 2 resultados en la consulta: uno para las filas afectadas por el INSERT, y otro para las filas devueltas por el SELECT. Para recuperar las filas devueltas por el SELECT, la función `sqlsrv_next_result` debe ser llamada para pasar el primer resultado.

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array("Database"=>"dbName", "UID"=>"userName", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

$query = "INSERT INTO Table_1 (id, data) VALUES (?,?); SELECT * FROM TABLE_1;";
$params = array(1, "some data");
$stmt = sqlsrv_query($conn, $query, $params);

// Consume el primer resultado (filas afectadas por el INSERT) sin llamar a la función sqlsrv_next_result.
echo "Filas afectadas : ".sqlsrv_rows_affected($stmt)."<br />";

// Se mueve al siguiente resultado y muestra los resultados.
$next_result = sqlsrv_next_result($stmt);
if( $next_result ) {
   while( $row = sqlsrv_fetch_array( $stmt, SQLSRV_FETCH_ASSOC)){
      echo $row['id']." : ".$row['data']."<br />";
   }
} elseif( is_null($next_result)) {
     echo "No hay más resultados.<br />";
} else {
     die(print_r(sqlsrv_errors(), true));
}
?>

   
```php

## Véase también

sqlsrv_query

sqlsrv_fetch_array

sqlsrv_rows_affected
