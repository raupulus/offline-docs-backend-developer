---
title: oci_num_rows
description: Devuelve el número de filas afectadas durante el último comando Oracle
source_url: https://www.php.net/manual/es/function.oci-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57510
---

oci_num_rows

Devuelve el número de filas afectadas durante el último comando Oracle

## Descripción

```php
oci_num_rows(resource $statement): int
```php

Devuelve el número de filas afectadas durante el último comando Oracle.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

## Valores devueltos

Devuelve el número de filas afectadas, en forma de `int`, o `false` si ocurre un error

## Ejemplos

Ejemplo con `oci_num_rows`

```
<?php
$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, "create table emp2 as select * from employees");
oci_execute($stid);
echo oci_num_rows($stid) . " filas insertadas.<br />\n";
oci_free_statement($stid);

$stid = oci_parse($conn, "delete from emp2");
oci_execute($stid, OCI_DEFAULT);
echo oci_num_rows($stid) . " filas borradas.<br />\n";
oci_commit($conn);
oci_free_statement($stid);

$stid = oci_parse($conn, "drop table emp2");
oci_execute($stid);
oci_free_statement($stid);

oci_close($conn);
?>

    
```php

## Notas

> [!NOTE]
> Esta función *no devuelve* el número de filas seleccionadas. Para los comandos de tipo SELECT, esta función va a devolver el número de filas que han sido leídas en el buffer con `oci_fetch*`.
