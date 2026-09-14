---
title: sqlsrv_num_rows
description: Recupera el número de filas de un conjunto de resultados
source_url: https://www.php.net/manual/es/function.sqlsrv-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_revision: 6047c10c1
order: 86260
---

sqlsrv_num_rows

Recupera el número de filas de un conjunto de resultados

## Descripción

```php
sqlsrv_num_rows(resource $stmt): mixed
```php

Recupera el número de filas de un conjunto de resultados. Esta función requiere que el recurso de consulta haya sido creado con un cursor estático o keyset. Para más información, consulte las funciones `sqlsrv_query`, `sqlsrv_prepare`, o el capítulo [Especificar un tipo de cursor y seleccionar filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx) en la documentación de Microsoft SQLSRV.

## Parámetros

`stmt`  
La consulta desde la cual se devuelve el número total de filas. El recurso de consulta debe haber sido creado con un cursor estático o keyset. Para más información, consulte las funciones `sqlsrv_query`, `sqlsrv_prepare`, o el capítulo [Especificar un tipo de cursor y seleccionar filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx) en la documentación de Microsoft SQLSRV.

## Valores devueltos

Devuelve el número total de filas recuperadas en caso de éxito, y `false` si ocurre un error. Si se utiliza un cursor anterior (por omisión), o un cursor dinámico, se devolverá `false`.

## Ejemplos

Ejemplo con `sqlsrv_num_rows`

```
<?php
$server = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password" );
$conn = sqlsrv_connect( $server, $connectionInfo );

$sql = "SELECT * FROM Table_1";
$params = array();
$options =  array( "Scrollable" => SQLSRV_CURSOR_KEYSET );
$stmt = sqlsrv_query( $conn, $sql , $params, $options );

$row_count = sqlsrv_num_rows( $stmt );

if ($row_count === false)
   echo "Error al recuperar el número de filas.";
else
   echo $row_count;
?>

   
```php

## Véase también

sqlsrv_has_rows

sqlsrv_rows_affected
