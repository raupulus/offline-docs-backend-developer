---
title: Memcached::deleteMultiByKey
description: Elimina varios elementos de un servidor específico
source_url: https://www.php.net/manual/es/memcached.deletemultibykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/deletemultibykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46480
---

Memcached::deleteMultiByKey

Elimina varios elementos de un servidor específico

## Descripción

```php
public Memcached::deleteMultiByKey(string $server_key, array $keys, [int $time]): array
```php

`Memcached::deleteMultiByKey` es funcionalmente idéntica al método Memcached::deleteMulti, excepto que el argumento `server_key` puede ser utilizado para asociar las claves `keys` con un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`keys`  
Las claves a eliminar.

`time`  
El tiempo de espera del servidor antes de eliminar los elementos.

> [!NOTE]
> A partir de memcached 1.3.0 (publicado en 2009) esta funcionalidad ya no está soportada. Pasar un valor distinto de cero para `time` causará que la eliminación falle. Memcached::getResultCode devolverá `MEMCACHED_INVALID_ARGUMENTS`.

## Valores devueltos

Devuelve un array indexado por `keys`. Cada elemento es `true` si la clave correspondiente fue eliminada, o una de las constantes `Memcached::RES_*` si la eliminación correspondiente falló.

Memcached::getResultCode devolverá el código de resultado de la última operación de eliminación ejecutada, es decir, la operación de eliminación del último elemento de `keys`.

## Véase también

Memcached::delete, Memcached::deleteByKey, Memcached::deleteMulti
