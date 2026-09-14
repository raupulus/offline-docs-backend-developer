---
title: wincache_ucache_meminfo
description: Recupera información sobre el uso de memoria caché de usuario
source_url: https://www.php.net/manual/es/function.wincache-ucache-meminfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-meminfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 709e2ce20
order: 101790
---

wincache_ucache_meminfo

Recupera información sobre el uso de memoria caché de usuario

## Descripción

```php
wincache_ucache_meminfo(): array
```php

Recupera información sobre el uso de memoria caché del usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Array de metadatos sobre el uso de la memoria caché de usuario o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `memory_total` - cantidad de memoria en bytes asignado para la caché de usuario
- `memory_free` - cantidad de memoria libre en bytes disponible para la caché de usuario
- `num_used_blks` - número de bloques de memoria utilizados por el caché del usuario
- `num_free_blks` - número de bloques disponibles en la memoria de la caché del usuario
- `memory_overhead` - cantidad de memoria en bytes utilizado para las estructuras de los usuarios de caché interna

## Ejemplos

Ejemplo de `wincache_ucache_meminfo`

```
<pre>
<?php
print_r(wincache_ucache_meminfo());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [memory_total] => 5242880
        [memory_free] => 5215056
        [num_used_blks] => 6
        [num_free_blks] => 3
        [memory_overhead] => 176
    )

## Véase también

`wincache_fcache_fileinfo`, `wincache_fcache_meminfo`, `wincache_ocache_fileinfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
