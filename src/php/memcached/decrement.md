---
title: Memcached::decrement
description: Disminuye un valor numérico
source_url: https://www.php.net/manual/es/memcached.decrement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/decrement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46430
---

Memcached::decrement

Disminuye un valor numérico

## Descripción

```php
public Memcached::decrement(string $key, [int $offset], [int $initial_value], [int $expiry]): int
```php

`Memcached::decrement` disminuye el valor numérico de `offset` unidades. Si el elemento no es numérico, se emitirá un error. Si la operación intenta disminuir por debajo de 0, el nuevo valor será 0. `Memcached::decrement` establecerá el elemento al valor del parámetro `initial_value` si la clave no existe.

## Parámetros

`key`  
La clave del elemento a disminuir.

`offset`  
La cantidad con la que disminuir el elemento.

`initial_value`  
El valor a utilizar para definir el elemento si no existe.

`expiry`  
El tiempo de expiración en la definición del elemento.

## Valores devueltos

Devuelve el nuevo valor del elemento en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcached::decrement`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->set('counter', 5);
$n = $m->decrement('counter');
var_dump($n);

$n = $m->decrement('counter', 10);
var_dump($n);

var_dump($m->get('counter'));

$m->set('counter', 'abc');
$n = $m->increment('counter');
// ^ fallará debido a que el valor del elemento no es numérico
var_dump($n);
?>

    
```php

El ejemplo anterior mostrará:

    int(4)
    int(0)
    int(0)
    bool(false)

## Véase también

Memcached::increment, Memcached::incrementByKey, Memcached::decrementByKey
