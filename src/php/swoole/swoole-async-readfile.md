---
title: swoole_async_readfile
description: Lee un fichero de manera asíncrona
source_url: https://www.php.net/manual/es/function.swoole-async-readfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-async-readfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 8e2b78157
order: 90410
---

swoole_async_readfile

Lee un fichero de manera asíncrona

## Descripción

```php
swoole_async_readfile(string $filename, callable $callback): bool
```php

## Parámetros

`filename`  
El nombre del fichero a leer.

`callback`  
```php
callback(string $filename, string $content): mixed
```

`filename`  
El nombre del fichero.

`content`  
El contenido leído del fichero.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
