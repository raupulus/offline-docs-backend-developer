---
title: Swoole\Coroutine\Lock::trylock
description: Intenta adquirir el bloqueo sin bloquear
source_url: https://www.php.net/manual/es/swoole-coroutine-lock.trylock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/coroutine/lock/trylock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 91590
---

Swoole\Coroutine\Lock::trylock

Intenta adquirir el bloqueo sin bloquear

## Descripción

```php
public Swoole\Coroutine\Lock::trylock(): bool
```php

Al llamar a la operación de bloqueo, si el bloqueo ya está siendo mantenido por otra corrutina, la función devolverá inmediatamente false sin suspender la corrutina actual ni ceder el control de la CPU. Este diseño no bloqueante permite al llamador manejar flexiblemente situaciones de contención, como reintentar, abandonar o ejecutar otra lógica.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el bloqueo se adquirió con éxito, `false` si el bloqueo no está disponible.
