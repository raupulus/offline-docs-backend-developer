---
title: sqlsrv_server_info
description: Devuelve información sobre el servidor
source_url: https://www.php.net/manual/es/function.sqlsrv-server-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-server-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86320
---

sqlsrv_server_info

Devuelve información sobre el servidor

## Descripción

```php
sqlsrv_server_info(resource $conn): array
```php

Devuelve información sobre el servidor.

## Parámetros

`conn`  
El recurso de conexión que conecta el cliente y el servidor.

## Valores devueltos

Devuelve un array como se describe en la tabla siguiente:

| CurrentDatabase  | La base de datos conectada  |
|------------------|-----------------------------|
| SQLServerVersion | La versión del servidor SQL |
| SQLServerName    | El nombre del servidor      |

Array devuelto

## Ejemplos

Ejemplo con `sqlsrv_server_info`

```
<?php
$serverName = "serverName\sqlexpress";
$conn = sqlsrv_connect( $serverName);
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

$server_info = sqlsrv_server_info( $conn);
if( $server_info )
{
    foreach( $server_info as $key => $value) {
       echo $key.": ".$value."<br />";
    }
} else {
      die( print_r( sqlsrv_errors(), true));
}
?>

   
```php

## Véase también

sqlsrv_client_info
