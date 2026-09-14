---
title: array_first
description: Obtiene el primer valor de un array
source_url: https://www.php.net/manual/es/function.array-first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: b68b5e427
order: 5310
---

array_first

Obtiene el primer valor de un array

## Descripción

```php
array_first(array $array): mixed
```php

Obtiene el primer valor del `array` dado.

## Parámetros

`array`  
Un array.

## Valores devueltos

Devuelve el primer valor de `array` si el array no está vacío; `null` en caso contrario.

## Ejemplos

Uso básico de `array_first`

```
<?php
$array = [1 => 'a', 0 => 'b', 3 => 'c', 2 => 'd'];

$firstValue = array_first($array);

var_dump($firstValue);
?>

   
```php

El ejemplo anterior mostrará:

    string(1) "a"

## Véase también

array_key_first

array_last
