---
title: Memcached::add
description: Añade un nuevo elemento bajo una nueva clave
source_url: https://www.php.net/manual/es/memcached.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46340
---

Memcached::add

Añade un nuevo elemento bajo una nueva clave

## Descripción

```php
public Memcached::add(string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::add` es similar a Memcached::set, pero la operación falla si la clave `key` ya existe.

## Parámetros

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode devuelve la constante `Memcached::RES_NOTSTORED` si la clave ya existe.

## Véase también

Memcached::addByKey, Memcached::set, Memcached::replace
