---
title: Swoole\Process::signal
description: Envía un signal a los procesos hijos.
source_url: https://www.php.net/manual/es/swoole-process.signal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/process/signal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 322606e4f
order: 92370
---

Swoole\Process::signal

Envía un signal a los procesos hijos.

## Descripción

```php
public static Swoole\Process::signal(string $signal_no, callable $callback): void
```php

## Parámetros

`signal_no`  

`callback`  

## Valores devueltos

Si el signal es enviado con éxito, devuelve TRUE, de lo contrario devuelve FALSE.
