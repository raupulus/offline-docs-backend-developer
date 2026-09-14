---
title: oci_field_is_null
description: Comprueba si un campo de la fila recuperada es nulo
source_url: https://www.php.net/manual/es/function.oci-field-is-null.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-field-is-null.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57340
---

oci_field_is_null

Comprueba si un campo de la fila recuperada es nulo

## Descripción

```php
oci_field_is_null(resource $statement, string $column): bool
```php

Verifica si el campo `column` dado de la fila actual de la consulta `statement` es nulo.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

`column`  
Puede ser el índice del campo (a partir de 1) o su nombre.

## Valores devueltos

Devuelve `true` si `column` es nulo, `false` en caso contrario.

## Ejemplos

Ejemplo con `oci_field_name`

```
<?php

// Creación de la tabla con:
//   CREATE TABLE mytab (c1 NUMBER);
//   INSERT INTO mytab VALUES (1);
//   INSERT INTO mytab VALUES (NULL);

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, "SELECT * FROM mytab");
oci_execute($stid);

while (($row = oci_fetch_array($stid, OCI_RETURN_NULLS)) != false) {
    $ncols = oci_num_fields($stid);
    for ($col = 1; $col <= $ncols; $col++) {
        var_dump(oci_field_is_null($stid, $col));
    }
}

// Muestra:
//    bool(false)
//    bool(true)

oci_free_statement($stid);
oci_close($conn);

?>

    
```php
