---
title: array_pop
description: Desapila un elemento del final de un array
source_url: https://www.php.net/manual/es/function.array-pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: d93972fb2
order: 5490
---

array_pop

Desapila un elemento del final de un array

## Descripción

```php
array_pop(array $array): mixed
```php

`array_pop` desapila y devuelve el valor del último elemento del array `array`, acortándolo en un elemento.

> [!NOTE]
> Esta función ejecutará `reset` sobre el puntero del `array` de entrada después de usarlo.

## Parámetros

`array`  
El array del cual se recupera el valor.

## Valores devueltos

Devuelve el valor del último elemento del array `array`. Si `array` está vacío, `null` será devuelto.

## Ejemplos

Ejemplo con `array_pop`

```
<?php
$stack = array("orange", "banana", "apple", "raspberry");
$fruit = array_pop($stack);
print_r($stack);
?>

    
```php

Después de esto, `$stack` tendrá solo 3 elementos:

```
Array
(
    [0] => orange
    [1] => banana
    [2] => apple
)

    
```php

y `raspberry` será asignado a `$fruit`.

## Véase también

`array_push`, `array_shift`, `array_unshift`
