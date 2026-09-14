---
title: oci_fetch
description: Lee la siguiente línea de un resultado Oracle en un buffer interno
source_url: https://www.php.net/manual/es/function.oci-fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5fcbcd6b5
order: 57330
---

oci_fetch

Lee la siguiente línea de un resultado Oracle en un buffer interno

## Descripción

```php
oci_fetch(resource $statement): bool
```php

Lee la siguiente línea de una consulta en un buffer interno accesible bien mediante la función `oci_result`, o utilizando las variables previamente definidas con la función `oci_define_by_name`.

Consulte la función `oci_fetch_array` para obtener información genérica sobre la recuperación de datos.

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

## Valores devueltos

Devuelve `true` en caso de éxito, o `false` si no hay más líneas disponibles para la consulta `statement`.

## Ejemplos

Ejemplo con `oci_fetch` y variables definidas

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$sql = 'SELECT location_id, city FROM locations WHERE location_id < 1200';
$stid = oci_parse($conn, $sql);

// La definición debe realizarse ANTES de la ejecución
oci_define_by_name($stid, 'LOCATION_ID', $locid);
oci_define_by_name($stid, 'CITY', $city);

oci_execute($stid);

// Cada recuperación utiliza las variables previamente definidas con los datos de la siguiente línea
while (oci_fetch($stid)) {
    echo "Location id $locid is $city<br>\n";
}

// Muestra:
//   Location id 1000 is Roma
//   Location id 1100 is Venice

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

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
    echo oci_result($stid, 'LOCATION_ID') . " is ";
    echo oci_result($stid, 'CITY') . "<br>\n";
}

// Muestra:
//   1000 is Roma
//   1100 is Venice

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Notas

> [!NOTE]
> Esta función no devolverá líneas desde el conjunto de resultados implícito de una base de datos Oracle. Utilice en su lugar la función `oci_fetch_array`.

## Véase también

`oci_define_by_name`, `oci_fetch_all`, `oci_fetch_array`, `oci_fetch_assoc`, `oci_fetch_object`, `oci_fetch_row`, `oci_result`
