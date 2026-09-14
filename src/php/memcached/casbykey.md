---
title: Memcached::casByKey
description: Comparar y cambiar un elemento en un servidor
source_url: https://www.php.net/manual/es/memcached.casbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/casbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46410
---

Memcached::casByKey

Comparar y cambiar un elemento en un servidor

## Descripción

```php
public Memcached::casByKey(string $cas_token, string $server_key, string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::casByKey` es funcionalmente equivalente a Memcached::cas, pero la variable `server_key` puede ser utilizada para dirigir la clave `key` a un servidor específico.

## Parámetros

`cas_token`  
Valor único, asociado a un elemento existente. Generado por memcache.

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode va devolver `Memcached::RES_DATA_EXISTS` si el elemento que se intenta almacenar ha sido modificado desde la última lectura.

## Véase también

Memcached::cas
