---
title: oci_num_fields
description: Devuelve el número de columnas en un resultado Oracle
source_url: https://www.php.net/manual/es/function.oci-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57500
---

oci_num_fields

Devuelve el número de columnas en un resultado Oracle

## Descripción

```php
oci_num_fields(resource $statement): int
```php

Devuelve el número de columnas en el resultado Oracle `statement`.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

## Valores devueltos

Devuelve el número de columnas, en forma de `int`.

## Ejemplos

Ejemplo con `oci_num_fields`

```
<?php

// Creación de la tabla con:
//   CREATE TABLE mytab (id NUMBER, quantity NUMBER);

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, "SELECT * FROM mytab");
oci_execute($stid, OCI_DESCRIBE_ONLY); // Uso de OCI_DESCRIBE_ONLY si no se recupera ninguna fila

$ncols = oci_num_fields($stid);
for ($i = 1; $i <= $ncols; $i++) {
    echo oci_field_name($stid, $i) . " " . oci_field_type($stid, $i) . "<br>\n";
}

// Muestra:
//    ID NUMBER
//    QUANTITY NUMBER

oci_free_statement($stid);
oci_close($conn);

?>

    
```php
