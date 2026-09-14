---
title: opcache_get_status
description: Obtiene información sobre el estado del caché
source_url: https://www.php.net/manual/es/function.opcache-get-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-get-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 87d6bb1bb
order: 58590
---

opcache_get_status

Obtiene información sobre el estado del caché

## Descripción

```php
opcache_get_status([bool $include_scripts]): array
```php

Esta función devuelve información sobre el estado de la instancia del caché en memoria. No devuelve información sobre el caché de ficheros.

## Parámetros

`include_scripts`  
Incluye información específica de los scripts.

## Valores devueltos

Devuelve un array de información, que opcionalmente contiene información específica de estado de un script, o `false` si ocurre un error.

## Errores/Excepciones

Si `opcache.restrict_api` está en uso y la ruta actual viola las reglas, se emitirá una advertencia E_WARNING; no se devolverá ninguna información de estado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PHP 8.3.0 | `opcache_get_status()['scripts'][n]['revalidate']` contiene ahora un timestamp Unix que indica cuándo se prevé la próxima revalidación del timestamp de los scripts, según lo dictado por la directiva INI [`opcache.revalidate_freq`](#ini.opcache.revalidate-freq). |

## Ejemplos

Un ejemplo de `opcache_get_status`

```
<?php
var_dump(opcache_get_status());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(9) {
      'opcache_enabled' =>
      bool(true)
      'cache_full' =>
      bool(false)
      'restart_pending' =>
      bool(false)
      'restart_in_progress' =>
      bool(false)
      'memory_usage' =>
      array(4) {
        'used_memory' =>
        int(9167936)
        'free_memory' =>
        int(125049792)
        'wasted_memory' =>
        int(0)
        'current_wasted_percentage' =>
        double(0)
      }
      'interned_strings_usage' =>
      array(4) {
        'buffer_size' =>
        int(8388608)
        'used_memory' =>
        int(2593616)
        'free_memory' =>
        int(5794992)
        'number_of_strings' =>
        int(10358)
      }
      'opcache_statistics' =>
      array(13) {
        'num_cached_scripts' =>
        int(0)
        'num_cached_keys' =>
        int(0)
        'max_cached_keys' =>
        int(16229)
        'hits' =>
        int(0)
        'start_time' =>
        int(1733310010)
        'last_restart_time' =>
        int(0)
        'oom_restarts' =>
        int(0)
        'hash_restarts' =>
        int(0)
        'manual_restarts' =>
        int(0)
        'misses' =>
        int(0)
        'blacklist_misses' =>
        int(0)
        'blacklist_miss_ratio' =>
        double(0)
        'opcache_hit_rate' =>
        double(0)
      }
      'scripts' =>
      array(0) {
      }
      'jit' =>
      array(7) {
        'enabled' =>
        bool(false)
        'on' =>
        bool(false)
        'kind' =>
        int(5)
        'opt_level' =>
        int(4)
        'opt_flags' =>
        int(6)
        'buffer_size' =>
        int(0)
        'buffer_free' =>
        int(0)
      }
    }

## Véase también

opcache_get_configuration
