---
title: oci_field_precision
description: Lee la precisión de un campo Oracle
source_url: https://www.php.net/manual/es/function.oci-field-precision.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-field-precision.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 5e41012cf
order: 57360
---

oci_field_precision

Lee la precisión de un campo Oracle

## Descripción

```php
oci_field_precision(resource $statement, string $column): int
```php

Devuelve la precisión del campo `column`.

Para las columnas de tipo FLOAT, la precisión no es nula, y la escala es de -127. Si la precisión es 0, entonces la columna es de tipo NUMBER. De lo contrario, es de tipo `NUMBER(precision, scale)`.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

`column`  
Puede ser un índice de campo (comenzando en 1) o un nombre de campo.

## Valores devueltos

Devuelve la precisión, en forma de `int`, o `false` si ocurre un error

## Ejemplos

Ejemplo con `oci_field_precision`

```
<?php

// Creación de la tabla con:
//   CREATE TABLE mytab (c1 NUMBER, c2 FLOAT, c3 NUMBER(4), c4 NUMBER(5,3));

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, "SELECT * FROM mytab");
oci_execute($stid, OCI_DESCRIBE_ONLY); // Uso de OCI_DESCRIBE_ONLY si ninguna fila es recuperada

$ncols = oci_num_fields($stid);
for ($i = 1; $i <= $ncols; $i++) {
    echo oci_field_name($stid, $i) . " "
        . oci_field_precision($stid, $i) . " "
        . oci_field_scale($stid, $i) . "<br>\n";
}

// Muestra:
//   C1    0 -127
//   C2  126 -127
//   C3    4    0
//   C4    5    3

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Véase también

`oci_field_scale`, `oci_field_type`
