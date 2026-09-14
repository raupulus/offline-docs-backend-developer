---
title: Ds\Set::reduce
description: Reduce el conjunto a un solo valor utilizando una función de retrollamada
source_url: https://www.php.net/manual/es/ds-set.reduce.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/reduce.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15950
---

Ds\Set::reduce

Reduce el conjunto a un solo valor utilizando una función de retrollamada

## Descripción

```php
public Ds\Set::reduce(callable $callback, [mixed $initial]): mixed
```php

Reduce el conjunto a un solo valor utilizando una función de retrollamada.

## Parámetros

`callback`  
```php
callback(mixed $carry, mixed $value): mixed
```

`carry`  
El valor de retorno de la retrollamada anterior, o `initial` si es la primera iteración.

`value`  
El valor de la iteración actual.

`initial`  
El valor inicial del valor de retorno. Puede ser `null`.

## Valores devueltos

El valor de retorno de la retrollamada final.

## Ejemplos

Ejemplo de `Ds\Set::reduce` con valor inicial

```php
<?php
$set = new \Ds\Set([1, 2, 3]);

$callback = function($carry, $value) {
    return $carry * $value;
};

var_dump($set->reduce($callback, 5));

// Iteraciones:
//
// $carry = $initial = 5
//
// $carry = $carry * 1 =  5
// $carry = $carry * 2 = 10
// $carry = $carry * 3 = 30
?>

   
```

Resultado del ejemplo anterior es similar a:

    int(30)

Ejemplo de `Ds\Set::reduce` sin valor inicial

```php
<?php
$set = new \Ds\Set([1, 2, 3]);

var_dump($set->reduce(function($carry, $value) {
    return $carry + $value + 5;
}));

// Iteraciones:
//
// $carry = $initial = null
//
// $carry = $carry + 1 + 5 =  6
// $carry = $carry + 2 + 5 = 13
// $carry = $carry + 3 + 5 = 21
?>

   
```

Resultado del ejemplo anterior es similar a:

    int(21)
