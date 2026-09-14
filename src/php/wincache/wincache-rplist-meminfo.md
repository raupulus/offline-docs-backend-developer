---
title: wincache_rplist_meminfo
description: Recupera información sobre el uso de la memoria por la caché de ruta
  de archivo resuelta
source_url: https://www.php.net/manual/es/function.wincache-rplist-meminfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-rplist-meminfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 709e2ce20
order: 101670
---

wincache_rplist_meminfo

Recupera información sobre el uso de la memoria por la caché de ruta de archivo resuelta

## Descripción

```php
wincache_rplist_meminfo(): array
```php

Recupera información sobre el uso de la memoria por la caché de ruta de archivo resuelta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de metadatos que describe el uso de la memoria por la caché de ruta de archivo resuelta. o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `memory_total` - cantidad de memoria, en bytes, asignada a la caché de rutas de archivos resueltas
- `memory_free` - cantidad de memoria libre, en bytes, disponible para la caché de rutas de archivos resueltas
- `num_used_blks` - número de bloques de memoria usados por la caché de rutas de archivos resueltas
- `num_free_blks` - número de bloques de memoria libres para la caché de rutas de archivos resueltas
- `memory_overhead` - cantidad de memoria, en bytes, usada para la estructura interna de la caché de rutas de archivos resueltas

## Ejemplos

Ejemplo con `wincache_rplist_meminfo`

```
<pre>
<?php
print_r(wincache_rplist_meminfo());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [memory_total] => 9437184
        [memory_free] => 9416744
        [num_used_blks] => 23
        [num_free_blks] => 1
        [memory_overhead] => 416
    )

## Véase también

`wincache_fcache_fileinfo`, `wincache_fcache_meminfo`, `wincache_ocache_fileinfo`, `wincache_ocache_meminfo`, `wincache_rplist_fileinfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
