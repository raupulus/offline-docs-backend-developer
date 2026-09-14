---
title: array_is_list
description: Verifica si un array dado es una lista
source_url: https://www.php.net/manual/es/function.array-is-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-is-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5380
---

array_is_list

Verifica si un

array

dado es una lista

## Descripción

```php
array_is_list(array $array): bool
```php

Determina si el `array` dado es una lista. Un `array` se considera como una lista si sus claves están compuestas por números consecutivos de `0` a `count($array)-1`.

## Parámetros

`array`  
El `array` en evaluación.

## Valores devueltos

Devuelve `true` si `array` es una lista, de lo contrario `false`.

## Ejemplos

Ejemplo de `array_is_list`

```
<?php
var_dump(array_is_list([])); // true
var_dump(array_is_list(['apple', 2, 3])); // true
var_dump(array_is_list([0 => 'apple', 'orange'])); // true

// El array no comienza en 0
var_dump(array_is_list([1 => 'apple', 'orange'])); // false

// Las claves no están en el orden correcto
var_dump(array_is_list([1 => 'apple', 0 => 'orange'])); // false

// Claves no enteras
var_dump(array_is_list([0 => 'apple', 'foo' => 'bar'])); // false

// Claves no consecutivas
var_dump(array_is_list([0 => 'apple', 2 => 'bar'])); // false
?>

    
```php

## Notas

> [!NOTE]
> Esta función devuelve `true` para los arrays vacíos.

## Véase también

`array_values`
