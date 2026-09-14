---
title: oci_new_cursor
description: Asigna y devuelve un nuevo cursor Oracle
source_url: https://www.php.net/manual/es/function.oci-new-cursor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-new-cursor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57480
---

oci_new_cursor

Asigna y devuelve un nuevo cursor Oracle

## Descripción

```php
oci_new_cursor(resource $connection): resource
```php

Asigna un nuevo cursor Oracle en la conexión especificada.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect` o la función `oci_pconnect`.

## Valores devueltos

Devuelve un nuevo manejador de conexión, o `false` si ocurre un error.

## Ejemplos

Utilizar un REF CURSOR de un procedimiento almacenado

```
<?php
// Requisitos previos:
//   crear o reemplazar el procedimiento myproc(myrc out sys_refcursor) de la siguiente manera:
//   begin
//     open myrc for select first_name from employees;
//   end;

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$curs = oci_new_cursor($conn);
$stid = oci_parse($conn, "begin myproc(:cursbv); end;");
oci_bind_by_name($stid, ":cursbv", $curs, -1, OCI_B_CURSOR);
oci_execute($stid);

oci_execute($curs);  // Ejecutar el REF CURSOR como un identificador de sentencia normal
while (($row = oci_fetch_array($curs, OCI_ASSOC+OCI_RETURN_NULLS)) != false) {
    echo $row['FIRST_NAME'] . "<br />\n";
}

oci_free_statement($stid);
oci_free_statement($curs);
oci_close($conn);
?>

    
```php
