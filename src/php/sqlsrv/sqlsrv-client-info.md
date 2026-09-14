---
title: sqlsrv_client_info
description: Devuelve información sobre el cliente y la conexión especificada
source_url: https://www.php.net/manual/es/function.sqlsrv-client-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-client-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86090
---

sqlsrv_client_info

Devuelve información sobre el cliente y la conexión especificada

## Descripción

```php
sqlsrv_client_info(resource $conn): array
```php

Devuelve información sobre el cliente y la conexión especificada

## Parámetros

`conn`  
La conexión sobre la que se va a retornar información.

## Valores devueltos

Devuelve un array asociativo con las claves que se describen en la tabla siguiente. Devuelve `false` en caso constrario.

| Clave         | Descripción                                                |
|---------------|------------------------------------------------------------|
| DriverDllName | SQLNCLI10.DLL                                              |
| DriverODBCVer | Versión ODBC (xx.yy)                                       |
| DriverVer     | Versión de la DLL del cliente nativo SQL Server (10.5.xxx) |
| ExtensionVer  | Versión de la biblioteca php_sqlsrv.dll (2.0.xxx.x)        |

Array devuelto por sqlsrv_client_info

## Ejemplos

Ejemplo de `sqlsrv_client_info`

```
<?php
$serverName = "serverName\sqlexpress";
$connOptions = array("UID"=>"username", "PWD"=>"password");
$conn = sqlsrv_connect( $serverName, $connOptions );

if( $conn === false ) {
    die( print_r( sqlsrv_errors(), true));
}

if( $client_info = sqlsrv_client_info( $conn)) {
    foreach( $client_info as $key => $value) {
        echo $key.": ".$value."<br />";
    }
} else {
    echo "Error al recuperar la información del cliente.<br />";
}
?>

   
```php

## Véase también

sqlsrv_server_info
