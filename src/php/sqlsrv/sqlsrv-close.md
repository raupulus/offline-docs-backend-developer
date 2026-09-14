---
title: sqlsrv_close
description: Cierra una conexión abierta y libera los recursos asociados a la conexión
source_url: https://www.php.net/manual/es/function.sqlsrv-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_revision: 6047c10c1
order: 86100
---

sqlsrv_close

Cierra una conexión abierta y libera los recursos asociados a la conexión

## Descripción

```php
sqlsrv_close(resource $conn): bool
```php

Cierra una conexión abierta y libera los recursos asociados a la conexión.

## Parámetros

`conn`  
La conexión que se va a cerrar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `sqlsrv_close`

```
<?php
$serverName = "serverName\sqlexpress";
$connOptions = array("UID"=>"username", "PWD"=>"password", "Database"=>"dbname");
$conn = sqlsrv_connect( $serverName, $connOptions );
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
}

//-------------------------------------
// Realizar aquí las operaciones contra la base de datos.
//-------------------------------------

// Cerrar la conexión.
sqlsrv_close( $conn );
?>

   
```php

## Véase también

sqlsrv_connect
