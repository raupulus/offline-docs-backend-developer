---
title: oci_field_type_raw
description: Lee los datos brutos del tipo de un campo
source_url: https://www.php.net/manual/es/function.oci-field-type-raw.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-field-type-raw.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57390
---

oci_field_type_raw

Lee los datos brutos del tipo de un campo

## Descripción

```php
oci_field_type_raw(resource $statement, string $column): int
```php

Lee los datos brutos "SQLT" del tipo del campo `column`.

Si se desea obtener el nombre del tipo del campo, utilice la función `oci_field_type`.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

`column`  
Puede ser el índice de un campo (comenzando en 1) o el nombre de un campo.

## Valores devueltos

Devuelve el tipo de datos brutos de Oracle, para el campo, en forma de número, o `false` si ocurre un error

## Ejemplos

Ejemplo con `oci_field_type_raw`

```
<?php

// Creación de la tabla con:
//   CREATE TABLE mytab (number_col NUMBER, varchar2_col varchar2(1), clob_col CLOB, date_col DATE);

$conn = oci_connect("hr", "hrpwd", "localhost/XE");
if (!$conn) {
    $m = oci_error();
    trigger_error(htmlentities($m['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, 'select * from mytab');
oci_execute($stid, OCI_DESCRIBE_ONLY);  // Uso de OCI_DESCRIBE_ONLY si no se recupera ninguna fila

$n = oci_num_fields($stid);
for ($i = 1; $i <= $n; ++$i) {
    echo oci_field_name($stid, $i) . " is raw type: " . oci_field_type_raw($stid, $i) . "<br>\n";
}

// Muestra:
//    NUMBER_COL is raw type: 2
//    VARCHAR2_COL is raw type: 1
//    CLOB_COL is raw type: 112
//    DATE_COL is raw type: 12

oci_free_statement($stid);
oci_close($conn);

?>
    
```php
