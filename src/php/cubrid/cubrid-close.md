---
title: cubrid_close
description: Cerrar la conexión de CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8610
---

cubrid_close

Cerrar la conexión de CUBRID

## Descripción

```php
cubrid_close([resource $conn_identifier]): bool
```php

La función `cubrid_close` termina la transacción en proceso actual, cierra el gestor de conexión y se desconecta del servidor. Si existe cualquier gestor de petición que no se haya cerrado todavía em este punto, éste se cerrará. Es similar a la función de CUBRID `cubrid_disconnect`.

## Parámetros

`conn_identifier`  
El identificador de conexión de CUBRID. Si no se especifica el identificador de conexión, se asume la última conexión abierta por `cubrid_connect`.

## Valores devueltos

`true`, cuando el proceso es satisfactorio.

`false`, cuando el proceso es insatisfactorio.

## Ejemplos

Ejemplo de `cubrid_close`

```
<?php
$con = cubrid_connect ("localhost", 33000, "demodb");
if ($con) {
   echo "conectado satisfactoriamente";
   $req = cubrid_execute ( $con, "insert into person values(1,'James')");
   if ($req) {
      cubrid_close_request ($req);
      cubrid_commit ($con);
   } else {
      cubrid_rollback ($con);
   }
   cubrid_close ($con);
}
?>

   
```php

## Véase también

cubrid_disconnect

cubrid_connect

cubrid_connect_with_url
