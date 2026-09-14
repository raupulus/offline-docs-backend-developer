---
title: array_push
description: Apila uno o más elementos al final de un array
source_url: https://www.php.net/manual/es/function.array-push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 627fb8f86
order: 5510
---

array_push

Apila uno o más elementos al final de un array

## Descripción

```php
array_push(array $array, mixed ...$values): int
```php

`array_push` considera `array` como una pila, y apila las variables `values` al final de `array`. La longitud del array `array` aumenta en consecuencia. Esto tiene el mismo efecto que:

```
<?php
$array[] = $var;
?>

   
```php

repetido para cada valor.

> [!NOTE]
> Si se utiliza la función `array_push` para añadir un elemento a un array, es preferible reemplazarla por el operador `$array[] =` que evita el paso por una función.

> [!NOTE]
> `array_push` emitirá una alerta si el primer argumento no es un array. Esto difiere del comportamiento de `$var[]` donde un nuevo array era creado, anteriormente a PHP 7.1.0.

## Parámetros

`array`  
El array de entrada.

`values`  
El valor a insertar al final del array `array`.

## Valores devueltos

Devuelve el nuevo número de elementos en el array.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | Esta función puede ahora ser llamada con un solo parámetro. Anteriormente, se requerían al menos dos parámetros. |

## Ejemplos

Ejemplo con `array_push`

```
<?php
$stack = array("orange", "banana");
array_push($stack, "apple", "raspberry");
print_r($stack);
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => orange
    [1] => banana
    [2] => apple
    [3] => raspberry
)

    
```php

## Véase también

`array_pop`, `array_shift`, `array_unshift`
