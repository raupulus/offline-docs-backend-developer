---
title: Memcache::getExtendedStats
description: Recupera estadísticas de todos los servidores en la lista
source_url: https://www.php.net/manual/es/memcache.getextendedstats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/getextendedstats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46170
---

Memcache::getExtendedStats

memcache_get_extended_stats

Recupera estadísticas de todos los servidores en la lista

## Descripción

```php
Memcache::getExtendedStats([string $type], [int $slabid], [int $limit]): array
```php

```php
memcache_get_extended_stats(Memcache $memcache, [string $type], [int $slabid], [int $limit]): array
```

`Memcache::getExtendedStats` devuelve un array asociativo de dos dimensiones con estadísticas de servidores. Las claves de los arrays corresponden a host:puerto de los servidores y los valores contienen estadísticas del servidor individual. Un servidor en fallo tendrá sus entradas correspondientes fijadas a `false`.

> [!NOTE]
> Esta función fue añadida en la versión 2.0.0 de Memcache.

## Parámetros

`type`  
El tipo de estadísticas a recuperar. Los valores válidos son: `"reset"`, `"malloc"`, `"maps"`, `"cachedump"`, `"slabs"`, `"items"`, `"sizes"`. Según las especificaciones del protocolo memcached, estos argumentos opcionales pueden ser modificados según las necesidades de los desarrolladores de memcache.

`slabid`  
Utilizado con el parámetro `type` definido como cachedump para identificar el slab a recuperar. El comando cachedump sobrecarga el servidor y solo debe ser utilizado con fines de depuración.

`limit`  
Utilizado con el parámetro `type` definido como cachedump para limitar el número de entradas a recuperar.

> [!WARNING]
> El tipo de estadística cachedump ha sido eliminado del proceso memcached por razones de seguridad.

## Valores devueltos

Devuelve un array asociativo con estadísticas de los servidores o `false` en caso de error.

## Ejemplos

Ejemplo con `Memcache::getExtendedStats`

```php
<?php
    $memcache_obj = new Memcache;
    $memcache_obj->addServer('memcache_host', 11211);
    $memcache_obj->addServer('failed_host', 11211);

    $stats = $memcache_obj->getExtendedStats();
    print_r($stats);
?>

   
```

El ejemplo anterior mostrará:

    Array
    (
        [memcache_host:11211] => Array
            (
                [pid] => 3756
                [uptime] => 603011
                [time] => 1133810435
                [version] => 1.1.12
                [rusage_user] => 0.451931
                [rusage_system] => 0.634903
                [curr_items] => 2483
                [total_items] => 3079
                [bytes] => 2718136
                [curr_connections] => 2
                [total_connections] => 807
                [connection_structures] => 13
                [cmd_get] => 9748
                [cmd_set] => 3096
                [get_hits] => 5976
                [get_misses] => 3772
                [bytes_read] => 3448968
                [bytes_written] => 2318883
                [limit_maxbytes] => 33554432
            )

        [failed_host:11211] => false
    )

## Véase también

Memcache::getVersion

Memcache::getStats
