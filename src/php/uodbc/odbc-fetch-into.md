---
title: odbc_fetch_into
description: Lee una línea de resultado y la coloca en un array
source_url: https://www.php.net/manual/es/function.odbc-fetch-into.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-fetch-into.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98820
---

odbc_fetch_into

Lee una línea de resultado y la coloca en un array

## Descripción

```php
odbc_fetch_into(Odbc\Result $statement, array $array, [int $row]): int
```php

Lee una línea de resultado y la coloca en un `array`.

## Parámetros

`statement`  
The ODBC result object.

`array`  
El `array` de resultado que puede ser de cualquier tipo, ya que será convertido en array. El array contendrá los valores de las columnas, estas últimas están numeradas a partir de 0.

`row`  
El número de la línea.

## Valores devueltos

Devuelve el número de columnas del resultado, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | `row` es ahora nullable. |

## Ejemplos

Ejemplo con `odbc_fetch_into`

```
<?php
$rc = odbc_fetch_into($res_id, $my_array);
?>

    
```php

o

```
<?php
$rc = odbc_fetch_into($res_id, $my_array, 2);
?>

    
```php
