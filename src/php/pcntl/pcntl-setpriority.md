---
title: pcntl_setpriority
description: Cambia la prioridad de un proceso
source_url: https://www.php.net/manual/es/function.pcntl-setpriority.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-setpriority.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 4ecb2c1b4
order: 61320
---

pcntl_setpriority

Cambia la prioridad de un proceso

## Descripción

```php
pcntl_setpriority(int $priority, [int $process_id], [int $mode]): bool
```php

`pcntl_setpriority` cambia la prioridad de `process_id`.

## Parámetros

`priority`  
`priority` es generalmente un valor que va de `-20` a `20`. La prioridad por omisión es `0` mientras que un valor numérico más pequeño favorece una mejor planificación. Como los niveles de prioridad cambian entre los tipos de sistemas y las versiones de kernel, lea la página de manual getpriority(2) de su sistema para detalles específicos.

`process_id`  
Si `null`, se utiliza el identificador del proceso actual.

`mode`  
Una constante entre `PRIO_PGRP`, `PRIO_USER`, `PRIO_PROCESS`, `PRIO_DARWIN_BG` o `PRIO_DARWIN_THREAD`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `process_id` es ahora nullable. |

## Véase también

`pcntl_getpriority`, `pcntl_setpriority`
