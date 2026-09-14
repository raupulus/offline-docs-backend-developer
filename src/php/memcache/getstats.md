---
title: Memcache::getStats
description: Lee las estadísticas del servidor
source_url: https://www.php.net/manual/es/memcache.getstats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/getstats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46190
---

Memcache::getStats

memcache_get_stats

Lee las estadísticas del servidor

## Descripción

```php
Memcache::getStats([string $type], [int $slabid], [int $limit]): array
```php

```php
memcache_get_stats(Memcache $memcache, [string $type], [int $slabid], [int $limit]): array
```

`Memcache::getStats` devuelve un array asociativo con las estadísticas del servidor. Los índices del array corresponden a los parámetros de estadísticas, y el valor asociado es el valor de dichas estadísticas.

## Parámetros

`type`  
El tipo de estadísticas a recuperar. Los valores válidos son {`"reset"`, `"malloc"`, `"maps"`, `"cachedump"`, `"slabs"`, `"items"`, `"sizes"`. Según las especificaciones del protocolo memcached, estos argumentos opcionales son susceptibles de ser modificados según las necesidades de los desarrolladores de memcache.

`slabid`  
Utilizado con el parámetro `type` definido como cachedump para identificar el slab a recuperar. El comando cachedump sobrecarga el servidor y no debe ser utilizado excepto para depuración.

`limit`  
Utilizado con el parámetro `type` definido como cachedump para limitar el número de entradas a recuperar.

## Valores devueltos

Devuelve un array asociativo de las estadísticas de un servidor o `false` si ocurre un error.

## Véase también

Memcache::getVersion

Memcache::getExtendedStats
