---
title: Swoole\Async::read
description: Lee de manera asíncrona un flujo de fichero.
source_url: https://www.php.net/manual/es/swoole-async.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/async/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 6047c10c1
order: 90700
---

Swoole\Async::read

Lee de manera asíncrona un flujo de fichero.

## Descripción

```php
public static Swoole\Async::read(string $filename, callable $callback, [int $chunk_size], [int $offset]): bool
```php

## Parámetros

`filename`  
El nombre del fichero.

`callback`  
```php
callback(string $filename, string $content): mixed
```

`filename`  
El nombre del fichero.

`content`  
El contenido leído desde el flujo de fichero.

`chunk_size`  
El tamaño del fragmento.

`offset`  
El desplazamiento.

## Valores devueltos

Si la lectura tiene éxito.
