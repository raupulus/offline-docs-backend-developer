---
title: wincache_ocache_fileinfo
description: Extrae información sobre los archivos almacenados en el caché opcode
source_url: https://www.php.net/manual/es/function.wincache-ocache-fileinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ocache-fileinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 101630
---

wincache_ocache_fileinfo

Extrae información sobre los archivos almacenados en el caché opcode

## Descripción

```php
wincache_ocache_fileinfo([bool $summaryonly]): array
```php

Extrae información sobre el contenido del caché opcode y su utilización.

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.0.0.

## Parámetros

`summaryonly`  
Controla si el array devuelto debe contener información sobre las entradas individuales del caché además del resumen del caché opcode.

## Valores devueltos

Array de metadatos sobre el caché opcode o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `total_cache_uptime` - Tiempo total de actividad en segundos del caché opcode
- `total_file_count` - Número total de archivos actualmente en el caché opcode
- `total_hit_count` - Número total de veces que el opcode compilado ha sido servido desde el caché
- `total_miss_count` - Número de veces que el opcode compilado no se encontró en el caché
- `is_local_cache` - true si los metadatos del caché son para una instancia de caché local, false si los metadatos son para el caché global.
- `file_entries` - Array que contiene información sobre todos los archivos almacenados en caché:
  - `file_name` - Nombre de archivo absoluto del archivo en caché
  - `add_time` - Tiempo en segundos desde que el archivo fue añadido al caché opcode
  - `use_time` - Tiempo en segundos desde que el archivo fue consultado en el caché opcode
  - `last_check` - Tiempo en segundos desde que el archivo fue verificado para cambios
  - `hit_count` - Número de veces que el archivo ha sido servido desde el caché
  - `function_count` - Número de funciones en el caché
  - `class_count` - Número de clases en el caché

## Ejemplos

Un ejemplo de `wincache_ocache_fileinfo`

```
<pre>
<?php
print_r(wincache_ocache_fileinfo());
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
        [file_entries] => Array
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

`wincache_fcache_fileinfo`, `wincache_fcache_meminfo`, `wincache_ocache_meminfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
