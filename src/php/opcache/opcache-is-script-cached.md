---
title: opcache_is_script_cached
description: Indica si un script está en el caché de OPCache
source_url: https://www.php.net/manual/es/function.opcache-is-script-cached.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-is-script-cached.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 3c36a56c9
order: 58620
---

opcache_is_script_cached

Indica si un script está en el caché de OPCache

## Descripción

```php
opcache_is_script_cached(string $filename): bool
```php

Esta función verifica si un script PHP ha sido almacenado en el caché de OPCache. Esto puede ser utilizado para detectar fácilmente las "alertas" del caché para un script en particular. Esta función solo verifica el caché en memoria, no el caché de ficheros. Para verificar el caché de ficheros, utilice `opcache_is_script_cached_in_file_cache`.

## Parámetros

`filename`  
La ruta de acceso al script PHP a verificar.

## Valores devueltos

Retorna `true` si el script `filename` está presente en el caché en memoria de OPCache, `false` en caso contrario.

## Véase también

opcache_compile_file

opcache_is_script_cached_in_file_cache
