---
title: wincache_scache_info
description: Recupera información sobre archivos almacenados en el caché de sesión.
source_url: https://www.php.net/manual/es/function.wincache-scache-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-scache-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 101680
---

wincache_scache_info

Recupera información sobre archivos almacenados en el caché de sesión.

## Descripción

```php
wincache_scache_info([bool $summaryonly]): array
```php

Recupera información sobre el contenido del caché de sesión y su utilización.

## Parámetros

`summaryonly`  
Controla si el array devuelto debe contener información sobre entradas individuales del caché además del resumen del caché.

## Valores devueltos

Un array de metadatos sobre el caché para esta sesión o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `total_cache_uptime` - duración total (en segundos) de activación del caché
- `total_item_count` - número total de elementos contenidos actualmente en el caché
- `is_local_cache` - `true` si los metadatos del caché son para una instancia de caché local, `false` si son para un caché global
- `total_hit_count` - número total de veces que los datos han sido servidos desde el caché
- `total_miss_count` - número total de veces que los datos no se encontraron en el caché
- `scache_entries` - un array que contiene información sobre los elementos almacenados en caché:
  - `key_name` - nombre de la clave usada para almacenar los datos
  - `value_type` - tipo del valor almacenado
  - `use_time` - tiempo, en segundos, desde el último acceso del archivo desde el caché opcode
  - `last_check` - tiempo, en segundos, desde la última vez que el archivo fue verificado para detectar cambios
  - `ttl_seconds` - tiempo restante antes de la eliminación de los datos del caché, 0 significa que nunca serán eliminados
  - `age_seconds` - tiempo transcurrido desde el momento en que se agregaron los datos en la caché
  - `hitcount` - número de veces que los datos han sido servidos desde el caché

## Ejemplos

Ejemplo con `wincache_scache_info`

```
<pre>
<?php
print_r(wincache_scache_info());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [total_cache_uptime] => 17357
        [total_file_count] => 121
        [total_hit_count] => 36562
        [total_miss_count] => 201
        [scache_entries] => Array
            (
                [1] => Array
                    (
                        [file_name] => c:\inetpub\wwwroot\checkcache.php
                        [add_time] => 17356
                        [use_time] => 7
                        [last_check] => 10
                        [hit_count] => 454
                        [function_count] => 0
                        [class_count] => 1
                    )
                [2] => Array (...iterates for each cached file)
            )
    )

## Véase también

`wincache_fcache_fileinfo`, `wincache_fcache_meminfo`, `wincache_ocache_meminfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_meminfo`
