---
title: swoole_async_write
description: Escribe datos en un flujo de fichero de manera asíncrona
source_url: https://www.php.net/manual/es/function.swoole-async-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-async-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 86e6094e8
order: 90430
---

swoole_async_write

Escribe datos en un flujo de fichero de manera asíncrona

## Descripción

```php
swoole_async_write(string $filename, string $content, [int $offset], [callable $callback]): bool
```php

## Parámetros

`filename`  
El nombre del fichero a escribir.

`content`  
El contenido a escribir en el fichero.

`offset`  
El desplazamiento.

`callback`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
