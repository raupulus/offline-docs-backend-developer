---
title: realpath_cache_size
description: Obtiene el tamaño del caché realpath
source_url: https://www.php.net/manual/es/function.realpath-cache-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/realpath-cache-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23970
---

realpath_cache_size

Obtiene el tamaño del caché realpath

## Descripción

```php
realpath_cache_size(): int
```php

Obtiene la cantidad de memoria utilizada por el caché realpath.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la cantidad de memoria utilizada por el caché realpath.

## Ejemplos

Ejemplo con `realpath_cache_size`

```
<?php
var_dump(realpath_cache_size());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(412)

## Véase también

`realpath_cache_get`, La opción de configuración [realpath_cache_size](#ini.realpath-cache-size)
