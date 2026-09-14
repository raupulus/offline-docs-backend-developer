---
title: wincache_rplist_fileinfo
description: Recupera información de la caché sobre una ruta de archivo resuelta
source_url: https://www.php.net/manual/es/function.wincache-rplist-fileinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-rplist-fileinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 709e2ce20
order: 101660
---

wincache_rplist_fileinfo

Recupera información de la caché sobre una ruta de archivo resuelta

## Descripción

```php
wincache_rplist_fileinfo([bool $summaryonly]): array
```php

Recupera información sobre las asignaciones almacenadas en caché entre rutas de archivos relativas y sus correspondencias en rutas de archivos absolutas

## Parámetros

`summaryonly`  

## Valores devueltos

Un array de metadatos con información sobre la caché de una ruta de archivo resuelta o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `total_file_count` - número total de rutas de archivos almacenadas en la caché
- `rplist_entries` - un array que contiene la información sobre las rutas de archivo presentes en la caché:
  - `resolve_path` - ruta hacia el archivo
  - `subkey_data` - ruta absoluta correspondiente

## Ejemplos

Ejemplo con `wincache_rplist_fileinfo`

```
<pre>
<?php
print_r(wincache_rplist_fileinfo());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [total_file_count] => 5
        [rplist_entries] => Array
            (
                [1] => Array
                    (
                        [resolve_path] => checkcache.php
                        [subkey_data] => c:\inetpub\wwwroot|c:\inetpub\wwwroot\checkcache.php
                    )

                [2] => Array (...iterates for each cached file)
            )
    )

## Véase también

`wincache_fcache_meminfo`, `wincache_fcache_fileinfo`, `wincache_ocache_fileinfo`, `wincache_ocache_meminfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
