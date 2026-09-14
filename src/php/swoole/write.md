---
title: Swoole\Async::write
description: Escribe de manera asíncrona datos en un flujo de fichero.
source_url: https://www.php.net/manual/es/swoole-async.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/async/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 90730
---

Swoole\Async::write

Escribe de manera asíncrona datos en un flujo de fichero.

## Descripción

```php
public static Swoole\Async::write(string $filename, string $content, [int $offset], [callable $callback]): void
```php

## Parámetros

`filename`  
El nombre del fichero en el cual escribir.

`content`  
El contenido a escribir en el fichero.

`offset`  
El desplazamiento.

`callback`
