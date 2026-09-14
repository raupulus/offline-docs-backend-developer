---
title: array_change_key_case
description: Cambia la casse de todas las claves de un array
source_url: https://www.php.net/manual/es/function.array-change-key-case.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-change-key-case.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 58d11dfe1
order: 5160
---

array_change_key_case

Cambia la casse de todas las claves de un array

## Descripción

```php
array_change_key_case(array $array, [int $case]): array
```php

Modifica las claves del array `array` y fuerza su casse. Esta función dejará las claves numéricas sin cambios.

## Parámetros

`array`  
El array a tratar

`case`  
O bien `CASE_UPPER` (mayúsculas), o bien `CASE_LOWER` (minúsculas, valor por omisión)

## Valores devueltos

Devuelve un array cuyas claves han sido transformadas en mayúsculas o en minúsculas.

## Ejemplos

Ejemplo con `array_change_key_case`

```
<?php
$input_array = array("FirSt" => 1, "SecOnd" => 4);
print_r(array_change_key_case($input_array, CASE_UPPER));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [FIRST] => 1
        [SECOND] => 4
    )

## Notas

> [!NOTE]
> Si un array posee claves que serán idénticas al ejecutar esta función (e.g. "`clé`" y "`CLé`"), el último valor en el array sobrescribirá los anteriores.
