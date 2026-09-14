---
title: array_last
description: Obtiene el último valor de un array
source_url: https://www.php.net/manual/es/function.array-last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: b68b5e427
order: 5430
---

array_last

Obtiene el último valor de un array

## Descripción

```php
array_last(array $array): mixed
```php

Obtiene el último valor del `array` dado.

## Parámetros

`array`  
Un array.

## Valores devueltos

Devuelve el último valor de `array` si el array no está vacío; `null` en caso contrario.

## Ejemplos

Uso básico de `array_last`

```
<?php
$array = [1 => 'a', 0 => 'b', 3 => 'c', 2 => 'd'];

$lastValue = array_last($array);

var_dump($lastValue);
?>

   
```php

El ejemplo anterior mostrará:

    string(1) "d"

## Véase también

array_key_last

array_first
