---
title: swoole_async_writefile
description: Escribe datos en un fichero de manera asíncrona
source_url: https://www.php.net/manual/es/function.swoole-async-writefile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-async-writefile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 322606e4f
order: 90440
---

swoole_async_writefile

Escribe datos en un fichero de manera asíncrona

## Descripción

```php
swoole_async_writefile(string $filename, string $content, [callable $callback], [int $flags]): bool
```php

## Parámetros

`filename`  
El nombre del fichero a escribir.

`content`  
El contenido a escribir en el fichero.

`callback`  

`flags`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
