---
title: memcache_debug
description: Activa/desactiva debug output
source_url: https://www.php.net/manual/es/function.memcache-debug.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/functions/memcache-debug.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_revision: f4098e2ba
order: 46070
---

memcache_debug

Activa/desactiva debug output

## Descripción

```php
memcache_debug(bool $on_off): bool
```php

`memcache_debug` activa el debug output si el parámetro `on_off` es igual a `true` y lo desactiva si es igual a `false`.

> [!NOTE]
> Solamente se puede acceder a `memcache_debug` si PHP fue compilado con la opción --enable-debug y en este caso siempre retorna `true`. De lo contrario, esta función no tiene ningún efecto y siempre devuelve `false`.

## Parámetros

`on_off`  
Activa debug output si es igual a `true`. Desactiva debug output si es igual a `false`.

## Valores devueltos

Devuelve `true` si PHP fue compilado con la opción --enable-debug, de lo contrario devuelve `false`.
