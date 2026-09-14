---
title: Swoole\Coroutine\Lock::lock
description: Adquirir el bloqueo, bloqueando si es necesario
source_url: https://www.php.net/manual/es/swoole-coroutine-lock.lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/coroutine/lock/lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 91580
---

Swoole\Coroutine\Lock::lock

Adquirir el bloqueo, bloqueando si es necesario

## Descripción

```php
public Swoole\Coroutine\Lock::lock(): bool
```php

Al ejecutar la operación de bloqueo, si el bloqueo ya está siendo mantenido por otra corrutina, la corrutina actual cederá activamente el control de la CPU y entrará en un estado suspendido. Cuando la corrutina que mantiene el bloqueo llame a unlock(), la corrutina en espera será despertada y tratará de adquirir el bloqueo nuevamente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si el bloqueo fue adquirido exitosamente, `false` en caso contrario.
