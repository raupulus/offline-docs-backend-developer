---
title: cubrid_disconnect
description: Cerrar una conexión a una base de datos
source_url: https://www.php.net/manual/es/function.cubrid-disconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-disconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8970
---

cubrid_disconnect

Cerrar una conexión a una base de datos

## Descripción

```php
cubrid_disconnect([resource $conn_identifier]): bool
```php

La función `cubrid_disconnect` cierra el gestor de conexión y se desconecta del servidor. Si algún gestor de solicitud no se ha sido cerrado en este punto, será cerrado. Es similar a la función de CUBRID compatible con MySQL `cubrid_close`.

## Parámetros

`conn_identifier`  
Identificador de conexión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_disconnect`

```
<?php
$con = cubrid_connect ("localhost", 33000, "demodb");
if ($con) {
   echo "conectado con éxito";

   $req = cubrid_execute( $con, "create table person(id int,name char(10))");
   if ($req) {
      cubrid_close_request($req);
      cubrid_commit($con);
   } else {
      cubrid_rollback($con);
   }

   $req = cubrid_execute( $con, "insert into person values(1,'James')");
   if ($req) {
      cubrid_close_request($req);
      cubrid_commit($con);
   } else {
      cubrid_rollback($con);
   }
   cubrid_disconnect($con);
}
?>

   
```php

## Véase también

cubrid_close

cubrid_connect

cubrid_connect_with_url
