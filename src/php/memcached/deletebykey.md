---
title: Memcached::deleteByKey
description: Elimina un elemento de un servidor específico
source_url: https://www.php.net/manual/es/memcached.deletebykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/deletebykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46460
---

Memcached::deleteByKey

Elimina un elemento de un servidor específico

## Descripción

```php
public Memcached::deleteByKey(string $server_key, string $key, [int $time]): bool
```php

`Memcached::deleteByKey` es funcionalmente equivalente a Memcached::delete, excepto por la variable libre `server_key` que puede ser utilizada para dirigir la variable `key` a un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave a eliminar.

`time`  
La duración de espera para la eliminación.

> [!NOTE]
> A partir de memcached 1.3.0 (publicado en 2009) esta funcionalidad ya no está soportada. Pasar un valor distinto de cero para `time` causará que la eliminación falle. Memcached::getResultCode devolverá `MEMCACHED_INVALID_ARGUMENTS`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. El método Memcached::getResultCode devuelve `Memcached::RES_NOTFOUND` si la clave no existe.

## Véase también

Memcached::delete, Memcached::deleteMulti, Memcached::deleteMultiByKey
