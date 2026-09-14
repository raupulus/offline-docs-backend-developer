---
title: oci_field_size
description: Devuelve el tamaño de un campo Oracle
source_url: https://www.php.net/manual/es/function.oci-field-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-field-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 5e41012cf
order: 57380
---

oci_field_size

Devuelve el tamaño de un campo Oracle

## Descripción

```php
oci_field_size(resource $statement, string $column): int
```php

Devuelve el tamaño del campo `column` Oracle.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

`column`  
Puede ser el índice del campo (la indexación comienza en 1) o el nombre del campo.

## Valores devueltos

Devuelve el tamaño del campo `field` en bytes, o `false` si ocurre un error

## Ejemplos

Ejemplo con `oci_field_size`

```
<?php

// Creación de la tabla con:
//   CREATE TABLE mytab (number_col NUMBER, varchar2_col varchar2(1),
//                       clob_col CLOB, date_col DATE);

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, "SELECT * FROM mytab");
oci_execute($stid, OCI_DESCRIBE_ONLY); // Utilización de OCI_DESCRIBE_ONLY si ninguna fila es recuperada

echo "<table border=\"1\">\n";
echo "<tr>";
echo "<th>Name</th>";
echo "<th>Type</th>";
echo "<th>Length</th>";
echo "</tr>\n";

$ncols = oci_num_fields($stid);

for ($i = 1; $i <= $ncols; $i++) {
    $column_name  = oci_field_name($stid, $i);
    $column_type  = oci_field_type($stid, $i);
    $column_size  = oci_field_size($stid, $i);

    echo "<tr>";
    echo "<td>$column_name</td>";
    echo "<td>$column_type</td>";
    echo "<td>$column_size</td>";
    echo "</tr>\n";
}

echo "</table>\n";

// Muestra:
//    Name           Type       Length
//    NUMBER_COL    NUMBER        22
//    VARCHAR2_COL  VARCHAR2       1
//    CLOB_COL      CLOB        4000
//    DATE_COL      DATE           7

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Véase también

`oci_num_fields`, `oci_field_name`
