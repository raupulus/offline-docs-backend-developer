---
title: Memcached::getStats
description: Lee estadísticas del grupo de servidores
source_url: https://www.php.net/manual/es/memcached.getstats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getstats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 5e6bdba53
order: 46640
---

Memcached::getStats

Lee estadísticas del grupo de servidores

## Descripción

```php
public Memcached::getStats([string $type]): array
```php

`Memcached::getStats` devuelve un array que contiene el estado de todas las máquinas en funcionamiento. Consúltese el [protocolo memcached](https://github.com/memcached/memcached/blob/master/doc/protocol.txt) para más detalles sobre estas estadísticas.

## Parámetros

`type`  
El tipo de estadísticas a recuperar.

## Valores devueltos

Un array de estadísticas de servidores, una entrada por servidor, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcached::getStats`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

print_r($m->getStats());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [localhost:11211] => Array
            (
                [pid] => 4933
                [uptime] => 786123
                [threads] => 1
                [time] => 1233868010
                [pointer_size] => 32
                [rusage_user_seconds] => 0
                [rusage_user_microseconds] => 140000
                [rusage_system_seconds] => 23
                [rusage_system_microseconds] => 210000
                [curr_items] => 145
                [total_items] => 2374
                [limit_maxbytes] => 67108864
                [curr_connections] => 2
                [total_connections] => 151
                [connection_structures] => 3
                [bytes] => 20345
                [cmd_get] => 213343
                [cmd_set] => 2381
                [get_hits] => 204223
                [get_misses] => 9120
                [evictions] => 0
                [bytes_read] => 9092476
                [bytes_written] => 15420512
                [version] => 1.2.6
            )

    )
