---
title: Memcached::increment
description: Incrementa numéricamente un elemento
source_url: https://www.php.net/manual/es/memcached.increment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/increment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46660
---

Memcached::increment

Incrementa numéricamente un elemento

## Descripción

```php
public Memcached::increment(string $key, [int $offset], [int $initial_value], [int $expiry]): int
```php

`Memcached::increment` incrementa el valor numérico de `offset` unidades. Si el elemento no es numérico, se generará un error. `Memcached::increment` establecerá el elemento al valor del argumento `initial_value` si la clave no existe.

## Parámetros

`key`  
La clave del elemento a incrementar.

`offset`  
La cantidad con la que aumentar el elemento.

`initial_value`  
El valor a utilizar para definir el elemento si no existe.

`expiry`  
El tiempo de expiración para definir el elemento.

## Valores devueltos

Devuelve el nuevo valor del elemento, en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcached::increment`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->set('counter', 0);
$m->increment('counter');
$n = $m->increment('counter', 10);
var_dump($n);

$m->set('counter', 'abc');
$n = $m->increment('counter');
// ^ fallará debido a que el valor del elemento no es numérico
var_dump($n);
?>

    
```php

El ejemplo anterior mostrará:

    int(11)
    bool(false)

## Véase también

Memcached::decrement, Memcached::decrementByKey, Memcached::incrementByKey
