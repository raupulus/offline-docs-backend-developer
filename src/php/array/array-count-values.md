---
title: array_count_values
description: Cuenta las ocurrencias de cada valor distinto en un array
source_url: https://www.php.net/manual/es/function.array-count-values.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-count-values.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 6b56e6f44
order: 5200
---

array_count_values

Cuenta las ocurrencias de cada valor distinto en un array

## Descripción

```php
array_count_values(array $array): array
```php

`array_count_values` devuelve un array que contiene los valores del array `array` (que deben ser `int`s o `string`s) como claves y su frecuencia en `array` como valores.

## Parámetros

`array`  
El array de valores a contar

## Valores devueltos

Devuelve un array asociativo de valores con las claves correspondientes a `array` y sus números como valores.

## Errores/Excepciones

Lanza una alerta de nivel `E_WARNING` para cada elemento que no es `string` o `int`.

## Ejemplos

Ejemplo con `array_count_values`

```
<?php
$array = array(1, "hello", 1, "world", "hello");
print_r(array_count_values($array));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [1] => 2
        [hello] => 2
        [world] => 1
    )

## Véase también

`count`, `array_unique`, `array_values`, `count_chars`
