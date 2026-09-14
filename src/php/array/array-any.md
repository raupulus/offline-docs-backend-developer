---
title: array_any
description: Verifica que al menos un elemento del array valide la función de retrollamada
source_url: https://www.php.net/manual/es/function.array-any.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-any.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 5150
---

array_any

Verifica que al menos un elemento del

array

valide la función de retrollamada

## Descripción

```php
array_any(array $array, callable $callback): bool
```php

`array_any` devuelve `true`, si la función de retrollamada `callback` devuelve `true` para al menos un elemento. De lo contrario, la función devuelve `false`.

## Parámetros

`array`  
El `array` a recorrer.

`callback`  
La función de retrollamada a utilizar para verificar cada elemento, que debe respetar la siguiente firma:

```php
callback(mixed $value, mixed $key): bool
```

Si esta función devuelve `true`, `true` será devuelto por `array_any` y la función de retrollamada no será llamada para los otros elementos.

## Valores devueltos

La función devuelve `true`, si hay al menos un elemento para el cual la función de retrollamada `callback` devuelve `true`. De lo contrario, la función devuelve `false`.

## Ejemplos

Ejemplo con `array_any`

```php
<?php
$array = [
    'a' => 'perro',
    'b' => 'gato',
    'c' => 'vaca',
    'd' => 'pato',
    'e' => 'ganso',
    'f' => 'elefante'
];

// Verificar si el nombre de un animal tiene más de 5 letras.
var_dump(array_any($array, function (string $value) {
    return strlen($value) > 5;
}));

// Verificar si el nombre de un animal tiene menos de 3 letras.
var_dump(array_any($array, function (string $value) {
    return strlen($value) < 3;
}));

// Verificar si una clave de array no es una cadena.
var_dump(array_any($array, function (string $value, $key) {
   return !is_string($key);
}));
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(false)

## Véase también

array_all

array_filter

array_find

array_find_key
