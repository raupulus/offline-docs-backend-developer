---
title: Swoole\Process::kill
description: Envía una señal al proceso hijo.
source_url: https://www.php.net/manual/es/swoole-process.kill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/process/kill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: d35bf3025
order: 92320
---

Swoole\Process::kill

Envía una señal al proceso hijo.

## Descripción

```php
public static Swoole\Process::kill(int $pid, [int $signal_no]): bool
```php

Envía una señal al proceso hijo.

## Parámetros

`pid`  
El PID del proceso

`signal_no`  
La señal a enviar

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
