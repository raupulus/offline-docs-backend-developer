---
title: Swoole\Async::readFile
description: Lee un fichero de manera asíncrona.
source_url: https://www.php.net/manual/es/swoole-async.readfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/async/readfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 6047c10c1
order: 90710
---

Swoole\Async::readFile

Lee un fichero de manera asíncrona.

## Descripción

```php
public static Swoole\Async::readFile(string $filename, callable $callback): void
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
El contenido leído desde el fichero.
