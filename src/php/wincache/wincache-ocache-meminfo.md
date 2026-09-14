---
title: wincache_ocache_meminfo
description: Extrae información sobre la utilización del caché opcode
source_url: https://www.php.net/manual/es/function.wincache-ocache-meminfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ocache-meminfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 709e2ce20
order: 101640
---

wincache_ocache_meminfo

Extrae información sobre la utilización del caché opcode

## Descripción

```php
wincache_ocache_meminfo(): array
```php

Extrae información sobre la utilización de la memoria por el caché opcode.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Tabla de metadatos sobre la utilización de la memoria caché opcode o `false` si ocurre un error

La tabla devuelta por esta función contiene los siguientes elementos:

- `memory_total` - Cantidad de memoria en bytes, asignada para el caché opcode
- `memory_free` - Cantidad de memoria libre en bytes, disponible para el caché opcode
- `num_used_blks` - Número de bloques de memoria utilizados por el caché opcode
- `num_free_blks` - Número de bloques de memoria libres disponibles para el caché opcode
- `memory_overhead` - Cantidad de memoria en bytes utilizada para la estructura interna del caché opcode

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.0.0.

## Ejemplos

Un ejemplo de `wincache_ocache_meminfo`

```
<pre>
<?php
print_r(wincache_ocache_meminfo());
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [memory_total] => 134217728
        [memory_free] => 112106972
        [num_used_blks] => 15469
        [num_free_blks] => 4
        [memory_overhead] => 247600
    )

## Véase también

`wincache_fcache_fileinfo`, `wincache_fcache_meminfo`, `wincache_ocache_fileinfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`, `wincache_scache_meminfo`
