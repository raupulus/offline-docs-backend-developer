---
title: sqlsrv_send_stream_data
description: Envía datos desde el flujo al servidor
source_url: https://www.php.net/manual/es/function.sqlsrv-send-stream-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-send-stream-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86310
---

sqlsrv_send_stream_data

Envía datos desde el flujo al servidor

## Descripción

```php
sqlsrv_send_stream_data(resource $stmt): bool
```php

Envía datos desde el flujo al servidor. Hasta 8 Ko de datos son enviados en cada llamada.

## Parámetros

`stmt`  
Un recurso de petición devuelto por la función `sqlsrv_query` o por la función `sqlsrv_execute`.

## Valores devueltos

Devuelve `true` si aún hay datos por enviar, y `false` si no hay más.

## Ejemplos

Ejemplo con `sqlsrv_send_stream_data`

```
<?php
$serverName = "serverName\sqlexpress";
$connectionInfo = array( "Database"=>"dbName", "UID"=>"username", "PWD"=>"password" );
$conn = sqlsrv_connect( $serverName, $connectionInfo);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$sql = "UPDATE Table_1 SET data = ( ?) WHERE id = 100";

// Abre los datos como flujo y los coloca en el array $params.
$data = fopen( "data://text/plain,[ Contenido largo aquí. ]", "r");
$params = array( &$data);

// Prepara la petición. Uso del array $options para desactivar
// el comportamiento por omisión, que es enviar todos los datos del flujo
// al momento de la ejecución de la petición.
$options = array("SendStreamParamsAtExec"=>0);
$stmt = sqlsrv_prepare( $conn, $sql, $params, $options);

sqlsrv_execute( $stmt);

// Envía hasta 8 Ko de datos al servidor
// en cada llamada a la función sqlsrv_send_stream_data.
$i = 1;
while( sqlsrv_send_stream_data( $stmt)) {
      $i++;
}
echo "$i llamadas fueron realizadas.";
?>

   
```php

## Véase también

sqlsrv_prepare

sqlsrv_query
