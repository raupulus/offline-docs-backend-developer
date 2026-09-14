---
title: wincache_fcache_meminfo
description: Recupera información sobre el uso de memoria caché de ficheros
source_url: https://www.php.net/manual/es/function.wincache-fcache-meminfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-fcache-meminfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_revision: 709e2ce20
order: 101610
---

wincache_fcache_meminfo

Recupera información sobre el uso de memoria caché de ficheros

## Descripción

```php
wincache_fcache_meminfo(): array
```php

Recupera información sobre el uso de la memoria caché del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Array de meta datos sobre el uso de memoria caché de ficheros o `false` si ocurre un error

El array devuelta por esta función contiene los siguientes elementos:

- `memory_total` - cantidad de memoria en bytes asignados para la caché de ficheros
- `memory_free` - cantidad de memoria libre en bytes disponibles para la caché de ficheros
- `num_used_blks` - número de bloques de memoria utilizados por la caché de ficheros
- `num_free_blks` - número de bloques de memoria libre disponibles para la caché de ficheros
- `memory_overhead` - cantidad de memoria en bytes utilizados para las estructuras internas de la caché de ficheros

## Ejemplos

Un ejemplo de `wincache_fcache_meminfo`

```
<pre>
<?php
print_r(wincache_fcache_meminfo());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [memory_total] => 134217728
        [memory_free] => 131339120
        [num_used_blks] => 361
        [num_free_blks] => 3
        [memory_overhead] => 5856
    )

## Véase también

`wincache_fcache_fileinfo`, `wincache_ocache_fileinfo`, `wincache_ocache_meminfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
