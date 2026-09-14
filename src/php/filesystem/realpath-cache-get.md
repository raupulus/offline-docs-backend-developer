---
title: realpath_cache_get
description: Recupera las entradas del caché realpath
source_url: https://www.php.net/manual/es/function.realpath-cache-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/realpath-cache-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23960
---

realpath_cache_get

Recupera las entradas del caché realpath

## Descripción

```php
realpath_cache_get(): array
```php

Recupera las entradas del caché realpath.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de entradas del caché realpath. Las claves son los caminos originales y los valores son arrays de datos que contienen el camino resuelto, la fecha de expiración y otros parámetros guardados en caché.

## Ejemplos

Ejemplo con `realpath_cache_get`

```
<?php
var_dump(realpath_cache_get());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["/test"]=>
      array(4) {
        ["key"]=>
        int(123456789)
        ["is_dir"]=>
        bool(true)
        ["realpath"]=>
        string(5) "/test"
        ["expires"]=>
        int(1260318939)
      }
      ["/test/test.php"]=>
      array(4) {
        ["key"]=>
        int(987654321)
        ["is_dir"]=>
        bool(false)
        ["realpath"]=>
        string(12) "/root/test.php"
        ["expires"]=>
        int(1260318939)
      }
    }

## Véase también

`realpath_cache_size`
