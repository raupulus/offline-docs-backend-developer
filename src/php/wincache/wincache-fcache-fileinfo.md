---
title: wincache_fcache_fileinfo
description: Extrae información sobre los archivos almacenados en la caché de archivos
source_url: https://www.php.net/manual/es/function.wincache-fcache-fileinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-fcache-fileinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 101600
---

wincache_fcache_fileinfo

Extrae información sobre los archivos almacenados en la caché de archivos

## Descripción

```php
wincache_fcache_fileinfo([bool $summaryonly]): array
```php

Extrae información sobre el contenido de la caché de archivos y su utilización.

## Parámetros

`summaryonly`  
Controla si el array devuelto debe contener información sobre las entradas individuales del caché además del resumen del caché de archivos.

## Valores devueltos

Array de metadatos sobre la caché de archivos o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `total_cache_uptime` - Tiempo total de actividad en segundos de la caché de archivos
- `total_file_count` - Número total de archivos actualmente en la caché de archivos
- `total_hit_count` - Número de veces que los archivos han sido servidos desde la caché de archivos
- `total_miss_count` - Número de veces que los archivos no se encontraron en la caché de archivos
- `file_entries` - Array que contiene información sobre todos los archivos almacenados en caché:
  - `file_name` - Nombre y ruta absoluta del archivo en caché
  - `add_time` - Tiempo en segundos desde que el archivo fue añadido a la caché de archivos
  - `use_time` - Tiempo en segundos desde que el archivo fue consultado en la caché de archivos
  - `last_check` - Tiempo en segundos desde la última verificación de modificaciones
  - `hit_count` - Número de veces que el archivo ha sido servido desde la caché
  - `file_size` - Tamaño en bytes del archivo almacenado en caché

## Ejemplos

Un ejemplo de `wincache_fcache_fileinfo`

```
<pre>
<?php
print_r(wincache_fcache_fileinfo());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [total_cache_uptime] => 3234
        [total_file_count] => 5
        [total_hit_count] => 0
        [total_miss_count] => 1
        [file_entries] => Array
            (
                [1] => Array
                    (
                        [file_name] => c:\inetpub\wwwroot\checkcache.php
                        [add_time] => 1
                        [use_time] => 0
                        [last_check] => 1
                        [hit_count] => 1
                        [file_size] => 2435
                    )
                [2] => Array (...iterates for each cached file)
            )
    )

## Véase también

`wincache_fcache_meminfo`, `wincache_ocache_fileinfo`, `wincache_ocache_meminfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
