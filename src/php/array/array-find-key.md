---
title: array_find_key
description: Devuelve la clave del primer elemento que valida la función de retrollamada
source_url: https://www.php.net/manual/es/function.array-find-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-find-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 5290
---

array_find_key

Devuelve la clave del primer elemento que valida la función de retrollamada

## Descripción

```php
array_find_key(array $array, callable $callback): mixed
```php

`array_find_key` devuelve la clave del primer elemento de un `array` para el cual la función de retrollamada `callback` devuelve `true`. Si no se encuentra ningún elemento, la función devuelve `null`.

## Parámetros

`array`  
El `array` a recorrer.

`callback`  
La función de retrollamada a utilizar, que debe respetar la siguiente firma:

```php
callback(mixed $value, mixed $key): bool
```

Si esta función devuelve `true`, la clave del elemento será devuelta por `array_find_key` y la función de retrollamada no será llamada para los otros elementos.

## Valores devueltos

La función devuelve la clave del primer elemento para el cual la función de retrollamada `callback` devuelve `true`. Si no se encuentra ningún elemento, la función devuelve `null`.

## Ejemplos

Ejemplo con `array_find_key`

```php
<?php
$array = [
    'a' => 'perro',
    'b' => 'vaca',
    'c' => 'gato',
    'd' => 'pato',
    'e' => 'oie',
    'f' => 'elefante'
];

// Encontrar la clave del primer animal cuyo nombre tiene más de 5 caracteres.
var_dump(array_find_key($array, function (string $value) {
    return strlen($value) > 5;
}));

// Encontrar la clave del primer animal cuyo nombre comienza con f.
var_dump(array_find_key($array, function (string $value) {
    return str_starts_with($value, 'f');
}));

// Encontrar la clave del primer animal que es también la primera letra de su nombre.
var_dump(array_find_key($array, function (string $value, $key) {
   return $value[0] === $key;
}));

// Encontrar la clave del primer animal que valida una RegEx.
var_dump(array_find_key($array, function ($value, $key) {
   return preg_match('/^([a-f])$/', $key);
}));
?>

   
```

El ejemplo anterior mostrará:

    string(1) "e"
    NULL
    string(1) "c"
    string(1) "a"

## Véase también

array_find

array_all

array_any

array_filter

array_reduce
