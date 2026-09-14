---
title: opcache_is_script_cached_in_file_cache
description: Indica si un script está en la caché de archivos de OPCache
source_url: https://www.php.net/manual/es/function.opcache-is-script-cached-in-file-cache.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-is-script-cached-in-file-cache.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_revision: 5a33c90d3
order: 58610
---

opcache_is_script_cached_in_file_cache

Indica si un script está en la caché de archivos de OPCache

## Descripción

```php
opcache_is_script_cached_in_file_cache(string $filename): bool
```php

Esta función verifica si un script PHP ha sido almacenado en la caché de OPCache. Esto puede utilizarse para detectar más fácilmente el "calentamiento" de la caché para un script en particular. Esta función solo verifica la caché de archivos, no la caché en memoria. Para verificar la caché en memoria, use `opcache_is_script_cached`.

## Parámetros

`filename`  
La ruta al script PHP a verificar.

## Valores devueltos

Devuelve `true` si `filename` está en la caché de OPCache, `false` en caso contrario.

## Véase también

opcache_compile_file

opcache_is_script_cached
