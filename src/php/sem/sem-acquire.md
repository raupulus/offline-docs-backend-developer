---
title: sem_acquire
description: Reserva un semáforo
source_url: https://www.php.net/manual/es/function.sem-acquire.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/sem-acquire.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73520
---

sem_acquire

Reserva un semáforo

## Descripción

```php
sem_acquire(SysvSemaphore $semaphore, [bool $non_blocking]): bool
```php

`sem_acquire` se bloquea por omisión (si es necesario) hasta que el semáforo pueda ser reservado. Un proceso que intenta reservar un semáforo que ya ha reservado quedará en espera indefinida, si esta adquisición excede el número máximo de adquisiciones simultáneas (max_acquire).

Al final de un script, todos los semáforos reservados pero no liberados explícitamente, serán liberados automáticamente, y se generará una advertencia.

## Parámetros

`semaphore`  
`semaphore` es un recurso de semáforo, obtenido de la función `sem_get`.

`non_blocking`  
Especifica si el proceso no debe esperar la adquisición del semáforo. Si es `true`, la llamada devolverá `false` inmediatamente si un semáforo no puede ser adquirido inmediatamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `semaphore` ahora espera una `SysvSemaphore`; anteriormente, se esperaba un `resource`. |

## Véase también

sem_get

sem_release
