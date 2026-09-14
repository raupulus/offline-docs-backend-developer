---
title: Memcached::replace
description: Remplaza un elemento bajo una clave
source_url: https://www.php.net/manual/es/memcached.replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46730
---

Memcached::replace

Remplaza un elemento bajo una clave

## Descripción

```php
public Memcached::replace(string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::replace` es similar a Memcached::set, pero la operación fallará si la clave `key` no existe en el servidor.

## Parámetros

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode devuelve `Memcached::RES_NOTFOUND` si la clave no existe.

## Véase también

Memcached::replaceByKey, Memcached::set, Memcached::add
