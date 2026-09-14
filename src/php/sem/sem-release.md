---
title: sem_release
description: Libera un semáforo
source_url: https://www.php.net/manual/es/function.sem-release.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/sem-release.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73540
---

sem_release

Libera un semáforo

## Descripción

```php
sem_release(SysvSemaphore $semaphore): bool
```php

`sem_release` libera el semáforo `sem_identifier`, si ha sido reservado por el proceso actual, de lo contrario genera un error.

Tras liberar el semáforo, `sem_acquire` puede ser llamado para reservarlo nuevamente.

## Parámetros

`semaphore`  
Un semáforo, tal como devuelto por la función `sem_get`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `semaphore` ahora espera una `SysvSemaphore`; anteriormente, se esperaba un `resource`. |

## Véase también

sem_get

sem_acquire
