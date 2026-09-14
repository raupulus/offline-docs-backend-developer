---
title: Memcached::replaceByKey
description: Remplaza un elemento específico en un servidor designado
source_url: https://www.php.net/manual/es/memcached.replacebykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/replacebykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46740
---

Memcached::replaceByKey

Remplaza un elemento específico en un servidor designado

## Descripción

```php
public Memcached::replaceByKey(string $server_key, string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::replaceByKey` es funcionalmente equivalente a la función Memcached::replace, con la excepción de que la variable libre `server_key` puede ser utilizada para dirigir la clave `key` hacia un servidor específico. Esto es útil si se desea mantener un grupo de variables agrupadas en un servidor.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode va devolver `Memcached::RES_NOTSTORED` si la clave no existe.

## Véase también

Memcached::replace, Memcached::set, Memcached::add
