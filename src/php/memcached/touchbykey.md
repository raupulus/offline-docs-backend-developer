---
title: Memcached::touchByKey
description: Define una nueva expiración en un elemento de un servidor específico
source_url: https://www.php.net/manual/es/memcached.touchbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/touchbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46850
---

Memcached::touchByKey

Define una nueva expiración en un elemento de un servidor específico

## Descripción

```php
public Memcached::touchByKey(string $server_key, string $key, [int $expiration]): bool
```php

`Memcached::touchByKey` es equivalente al método Memcached::touch, excepto que el argumento `server_key` puede ser utilizado para ligar la clave `key` con un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave bajo la cual almacenar el valor.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Véase también

Memcached::touch
