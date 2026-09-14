---
title: Swoole\Coroutine\Lock::unlock
description: Liberar el bloqueo
source_url: https://www.php.net/manual/es/swoole-coroutine-lock.unlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/coroutine/lock/unlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 91600
---

Swoole\Coroutine\Lock::unlock

Liberar el bloqueo

## Descripción

```php
public Swoole\Coroutine\Lock::unlock(): bool
```php

## Comportamiento de desbloqueo

1.  *Con io_uring futex:* el sistema despertará precisamente una corrutina en la cola de espera.

2.  *Sin io_uring futex:* las corrutinas en espera deben esperar a que termine su tiempo de retroceso y competir para readquirir el bloqueo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el bloqueo se liberó correctamente, `false` en caso contrario.
