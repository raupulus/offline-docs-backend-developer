---
title: array_all
description: Verifica si todos los elementos del array validan la función de retrollamada
source_url: https://www.php.net/manual/es/function.array-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 5140
---

array_all

Verifica si todos los elementos del

array

validan la función de retrollamada

## Descripción

```php
array_all(array $array, callable $callback): bool
```php

`array_all` devuelve `true`, si la función de retrollamada `callback` devuelve `true` para todos los elementos. De lo contrario, la función devuelve `false`.

## Parámetros

`array`  
El `array` a recorrer.

`callback`  
La función de retrollamada a utilizar para validar cada elemento, que debe respetar la siguiente firma:

```php
callback(mixed $value, mixed $key): bool
```

Si esta función devuelve `false`, `false` será devuelto por `array_all` y la función de retrollamada no será llamada para los otros elementos.

## Valores devueltos

La función devuelve `true`, si `callback` devuelve `true` para cada elemento. De lo contrario, la función devuelve `false`.

## Ejemplos

Ejemplo con `array_all`

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

// Verificar si todos los nombres de animales tienen menos de 12 letras.
var_dump(array_all($array, function (string $value) {
    return strlen($value) < 12;
}));

// Verificar si todos los nombres de animales tienen más de 5 letras.
var_dump(array_all($array, function (string $value) {
    return strlen($value) > 5;
}));

// Verificar si todas las claves del array son strings.
var_dump(array_all($array, function (string $value, $key) {
   return is_string($key);
}));
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(true)

## Véase también

array_any

array_filter

array_find

array_find_key
