---
title: Memcached::touch
description: Define una nueva expiración en un elemento
source_url: https://www.php.net/manual/es/memcached.touch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/touch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46840
---

Memcached::touch

Define una nueva expiración en un elemento

## Descripción

```php
public Memcached::touch(string $key, [int $expiration]): bool
```php

`Memcached::touch` define un nuevo valor de expiración para una clave dada.

## Parámetros

`key`  
La clave bajo la cual almacenar el valor.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Véase también

Memcached::touchByKey
