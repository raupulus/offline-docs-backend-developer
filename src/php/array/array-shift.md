---
title: array_shift
description: Despila un elemento al principio de un array
source_url: https://www.php.net/manual/es/function.array-shift.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-shift.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: aba949332
order: 5580
---

array_shift

Despila un elemento al principio de un array

## Descripción

```php
array_shift(array $array): mixed
```php

`array_shift` extrae el primer valor del `array` `array` y lo devuelve, acortando `array` en un elemento, y desplazando todos los elementos hacia abajo. Todas las claves numéricas serán modificadas para comenzar en cero mientras que las claves literales no serán afectadas.

> [!NOTE]
> Esta función ejecutará `reset` sobre el puntero del `array` de entrada después de usarlo.

## Parámetros

`array`  
El array de entrada.

## Valores devueltos

Devuelve el valor despilado, o `null` si el array está vacío o si el valor de entrada no es un array.

## Ejemplos

Ejemplo con `array_shift`

```
<?php
$stack = array("orange", "banana", "apple", "raspberry");
$fruit = array_shift($stack);
print_r($stack);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => banana
    [1] => apple
    [2] => raspberry
)

    
```php

y `orange` ha sido colocado en `$fruit`.

## Véase también

`array_unshift`, `array_push`, `array_pop`
