---
title: oci_statement_type
description: Devuelve el tipo de consulta Oracle
source_url: https://www.php.net/manual/es/function.oci-statement-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-statement-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57680
---

oci_statement_type

Devuelve el tipo de consulta Oracle

## Descripción

```php
oci_statement_type(resource $statement): string
```php

Devuelve una palabra clave que identifica el tipo de la consulta `statement` OCI8.

## Parámetros

`statement`  
Un identificador de consulta OCI válido, devuelto por la función `oci_parse`.

## Valores devueltos

Devuelve el tipo de consulta `statement` en forma de una de las siguientes cadenas.

| Cadena devuelta | Notas |
|-----------------|-------|
| `ALTER`         |       |
| `BEGIN`         |       |
| `CALL`          |       |
| `CREATE`        |       |
| `DECLARE`       |       |
| `DELETE`        |       |
| `DROP`          |       |
| `INSERT`        |       |
| `SELECT`        |       |
| `UPDATE`        |       |
| `UNKNOWN`       |       |

Tipo de consulta

Devuelve `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_statement_type`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'DELETE FROM departments WHERE department_id = 130;');
if (oci_statement_type($stid) == "DELETE") {
    trigger_error('No se está autorizado a borrar líneas en esta tabla', E_USER_ERROR);
}
else {
    oci_execute($stid);  // borra la línea
}

oci_free_statement($stid);
oci_close($conn);

?>

    
```php
