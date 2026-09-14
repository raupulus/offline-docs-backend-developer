---
title: swoole_async_read
description: Lee un flujo de fichero de manera asíncrona
source_url: https://www.php.net/manual/es/function.swoole-async-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-async-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 6047c10c1
order: 90400
---

swoole_async_read

Lee un flujo de fichero de manera asíncrona

## Descripción

```php
swoole_async_read(string $filename, callable $callback, [int $chunk_size], [int $offset]): bool
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
El contenido leído del flujo de fichero.

`chunk_size`  
El tamaño del fragmento.

`offset`  
El desplazamiento.

## Valores devueltos

Si la lectura tiene éxito.
