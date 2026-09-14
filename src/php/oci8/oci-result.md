---
title: oci_result
description: Devuelve el valor de una columna en un resultado Oracle
source_url: https://www.php.net/manual/es/function.oci-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57560
---

oci_result

Devuelve el valor de una columna en un resultado Oracle

## Descripción

```php
oci_result(resource $statement, string $column): mixed
```php

Devuelve los datos de la columna `column` en la fila actual del resultado `statement`.

Para más detalles sobre el mapeo de tipos de datos realizado por la extensión OCI8, lea los [tipos de datos soportados por el driver](#oci8.datatypes).

## Parámetros

`statement`  

`column`  
Puede ser el número de la columna (empezando por 1), o el nombre de la columna. Si es el nombre de la columna, es porque las metadatos de Oracle lo presentan de esta manera, y estará en mayúsculas para las columnas creadas sin tener en cuenta la casilla.

## Valores devueltos

Devuelve todos los tipos, excepto los tipos abstractos (ROWIDs, LOBs y FILEs). Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `oci_fetch` y `oci_result`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$sql = 'SELECT location_id, city FROM locations WHERE location_id < 1200';
$stid = oci_parse($conn, $sql);
oci_execute($stid);

while (oci_fetch($stid)) {
    echo oci_result($stid, 'LOCATION_ID') . " es ";
    echo oci_result($stid, 'CITY') . "<br>\n";
}

// Muestra:
//   1000 es Roma
//   1100 es Venice

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Véase también

`oci_fetch_array`, `oci_fetch_assoc`, `oci_fetch_object`, `oci_fetch_row`, `oci_fetch_all`
