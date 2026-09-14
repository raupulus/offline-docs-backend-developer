---
title: Memcached::get
description: Lee un elemento
source_url: https://www.php.net/manual/es/memcached.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46520
---

Memcached::get

Lee un elemento

## Descripción

```php
public Memcached::get(string $key, [callable $cache_cb], [int $get_flags]): mixed
```php

`Memcached::get` lee un elemento que ha sido almacenado previamente con la clave `key`. Si el elemento es encontrado, y que `get_flags` es proporcionado `Memcached::GET_EXTENDED`, el valor del token CAS del elemento también será retornado. Ver Memcached::cas para saber cómo utilizar los tokens CAS. Una [función de retrollamada en caso de ausencia](#memcached.callbacks) puede ser especificada con el parámetro `cache_cb`.

## Parámetros

`key`  
La clave del elemento a leer.

`cache_cb`  
Una función de retrollamada en caso de ausencia o `null`.

`get_flags`  
Bandera para controlar el resultado retornado. Cuando `Memcached::GET_EXTENDED` es proporcionada, la función retornará también el token CAS.

## Valores devueltos

Retorna el valor almacenado en la caché, o bien `false` en caso contrario. Si `get_flags` es definido a `Memcached::GET_EXTENDED`, un `array` conteniendo el valor y el token CAS es retornado en lugar de solo el valor. El método Memcached::getResultCode retorna `Memcached::RES_NOTFOUND` si la clave no existe.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL memcached 3.0.0 | El parámetro `cas_tokens` ha sido eliminado. `Memcached::GET_EXTENDED` ha sido añadida y cuando es pasada como bandera asegura que los tokens CAS sean recuperados. |

## Ejemplos

Ejemplo con `Memcached::get` 1

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->set('foo', 100);
var_dump($m->get('foo'));
?>

    
```php

El ejemplo anterior mostrará:

    int(100)

Ejemplo con `Memcached::get` 2

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

if (!($ip = $m->get('ip_block'))) {
    if ($m->getResultCode() == Memcached::RES_NOTFOUND) {
        $ip = array();
        $m->set('ip_block', $ip);
    } else {
        /* log error */
        /* ...       */
    }
}
?>

    
```php

## Véase también

Memcached::getByKey, Memcached::getMulti, Memcached::getDelayed
