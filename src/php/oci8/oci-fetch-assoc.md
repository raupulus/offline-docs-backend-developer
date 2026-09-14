---
title: oci_fetch_assoc
description: Lee una línea de un resultado en forma de array asociativo
source_url: https://www.php.net/manual/es/function.oci-fetch-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-fetch-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57300
---

oci_fetch_assoc

Lee una línea de un resultado en forma de array asociativo

## Descripción

```php
oci_fetch_assoc(resource $statement): array
```php

Devuelve un array asociativo que contiene la siguiente línea de resultado de una consulta. Cada elemento del array corresponde a una columna de la línea. Esta función es típicamente llamada en un ciclo mientras no devuelva `false`, lo que indica que no hay más líneas disponibles.

`oci_fetch_assoc` es idéntica a la función `oci_fetch_array` y al modo `OCI_ASSOC` + `OCI_RETURN_NULLS`.

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

## Valores devueltos

Devuelve un array asociativo o `false` si no hay más líneas disponibles para la consulta `statement`.

## Ejemplos

Ejemplo con `oci_fetch_assoc`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT department_id, department_name FROM departments');
oci_execute($stid);

while (($row = oci_fetch_assoc($stid)) != false) {
    echo $row['DEPARTMENT_ID'] . " " . $row['DEPARTMENT_NAME'] . "<br>\n";
}

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Notas

> [!NOTE]
> Ver `oci_fetch_array` para más ejemplos sobre la recuperación de líneas.

## Véase también

`oci_fetch`, `oci_fetch_all`, `oci_fetch_array`, `oci_fetch_object`, `oci_fetch_row`
