---
title: Ds\Deque::reduce
description: Reduce el deque a un solo valor utilizando una función de retrollamada
source_url: https://www.php.net/manual/es/ds-deque.reduce.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/reduce.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14660
---

Ds\Deque::reduce

Reduce el deque a un solo valor utilizando una función de retrollamada

## Descripción

```php
public Ds\Deque::reduce(callable $callback, [mixed $initial]): mixed
```php

Reduce el deque a un solo valor utilizando una función de retrollamada.

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

Ejemplo de `Ds\Deque::reduce` con un valor inicial

```php
<?php
$deque = new \Ds\Deque([1, 2, 3]);

$callback = function($carry, $value) {
    return $carry * $value;
};

var_dump($deque->reduce($callback, 5));

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

Ejemplo de `Ds\Deque::reduce` sin valor inicial

```php
<?php
$deque = new \Ds\Deque([1, 2, 3]);

var_dump($deque->reduce(function($carry, $value) {
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
