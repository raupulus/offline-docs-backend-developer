---
title: array_find
description: Devuelve el primer elemento que valida la función de retrollamada
source_url: https://www.php.net/manual/es/function.array-find.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-find.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 5300
---

array_find

Devuelve el primer elemento que valida la función de retrollamada

## Descripción

```php
array_find(array $array, callable $callback): mixed
```php

`array_find` devuelve el valor del primer elemento del `array` para el cual la función de retrollamada `callback` devuelve `true`. Si ningún elemento es encontrado, la función devuelve `null`.

## Parámetros

`array`  
El `array` a recorrer.

`callback`  
La función de retrollamada a utilizar, que debe respetar la siguiente firma:

```php
callback(mixed $value, mixed $key): bool
```

Si esta función devuelve `true`, el valor del elemento será devuelto por `array_find` y la función de retrollamada no será llamada para los otros elementos.

## Valores devueltos

La función devuelve el valor del primer elemento para el cual el `callback` devuelve `true`. Si ningún elemento es encontrado, la función devuelve `null`.

## Ejemplos

Ejemplo con `array_find`

```php
<?php
$array = [
    'a' => 'perro',
    'b' => 'vaca',
    'c' => 'gato',
    'd' => 'pato',
    'e' => 'ganso',
    'f' => 'elefante'
];

// Encontrar el primer animal cuyo nombre tiene más de 5 caracteres.
var_dump(array_find($array, function (string $value) {
    return strlen($value) > 5;
}));

// Encontrar el primer animal cuyo nombre comienza con f.
var_dump(array_find($array, function (string $value) {
    return str_starts_with($value, 'f');
}));

// Encontrar el primer animal cuya clave es la primera letra de su nombre.
var_dump(array_find($array, function (string $value, $key) {
   return $value[0] === $key;
}));

// Encontrar el primer animal cuya clave valida una RegEx.
var_dump(array_find($array, function ($value, $key) {
   return preg_match('/^([a-f])$/', $key);
}));
?>

   
```

El ejemplo anterior mostrará:

    string(5) "pato"
    NULL
    string(3) "gato"
    string(3) "perro"

## Véase también

array_find_key

array_all

array_any

array_filter

array_reduce
