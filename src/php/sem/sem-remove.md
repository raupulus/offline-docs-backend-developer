---
title: sem_remove
description: Destruye un semáforo
source_url: https://www.php.net/manual/es/function.sem-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/sem-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73550
---

sem_remove

Destruye un semáforo

## Descripción

```php
sem_remove(SysvSemaphore $semaphore): bool
```php

`sem_remove` elimina el semáforo dado.

Tras la eliminación del semáforo, ya no es utilizable.

## Parámetros

`semaphore`  
Un semáforo, tal como es devuelto por la función `sem_get`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `semaphore` ahora espera una `SysvSemaphore`; anteriormente, se esperaba un `resource`. |

## Véase también

sem_get

sem_release

sem_acquire
