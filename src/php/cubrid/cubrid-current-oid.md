---
title: cubrid_current_oid
description: Obtener el OID de la posición del cursor actual
source_url: https://www.php.net/manual/es/function.cubrid-current-oid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-current-oid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8960
---

cubrid_current_oid

Obtener el OID de la posición del cursor actual

## Descripción

```php
cubrid_current_oid(resource $req_identifier): string
```php

La función `cubrid_current_oid` se usa para obtener el oid de la posición del cursor actual desde el resultado de la consulta. Para usar `cubrid_current_oid`, la consulta ejecutada debe ser una consulta actualizable, y se debe incluir la opción `CUBRID_INCLUDE_OID` durante la ejecución de la consulta.

## Parámetros

`req_identifier`  
Identificador de solicitud.

## Valores devueltos

Oid de la posición del cursor actual, cuando el proceso tiene éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_current_oid`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

$req = cubrid_execute($conn, "SELECT * FROM code", CUBRID_INCLUDE_OID);
$oid = cubrid_current_oid($req);
$res = cubrid_get($conn, $oid);

print_r($res);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [s_name] => X
        [f_name] => Mixed
    )

## Véase también

cubrid_execute
