---
title: cubrid_close_prepare
description: Cerrar el gestor de solicitud
source_url: https://www.php.net/manual/es/function.cubrid-close-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-close-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8870
---

cubrid_close_prepare

Cerrar el gestor de solicitud

## Descripción

```php
cubrid_close_prepare(resource $req_identifier): bool
```php

La función `cubrid_close_prepare` cierra el gestor de solicitud dado por el argumento `req_identifier`, y libera la región de memoria relacionada con el gestor. Es un alias de `cubrid_close_request`.

## Parámetros

`req_identifier`  
Identificador de solicitud.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo de `cubrid_close_prepare`

```
<?php
$con = cubrid_connect ("localhost", 33000, "demodb", "dba", "");
if ($con) {
   echo "conectado con éxito";
   $req = cubrid_execute ( $con, "select * from members",
                           CUBRID_INCLUDE_OID | CUBRID_ASYNC);
   if ($req) {
      while ( list ($id, $nombre) = cubrid_fetch ($req) ){
         echo $id;
         echo $nombre;
      }
      cubrid_close_prepare($req); // o se puede usar cubrid_close_request($req)
   }
   cubrid_disconnect($con);
}
?>

   
```php

## Véase también

cubrid_close_request
