---
title: pcntl_getpriority
description: Devuelve la prioridad de un proceso
source_url: https://www.php.net/manual/es/function.pcntl-getpriority.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-getpriority.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: e251b5cfd
order: 61270
---

pcntl_getpriority

Devuelve la prioridad de un proceso

## Descripción

```php
pcntl_getpriority([int $process_id], [int $mode]): int
```php

`pcntl_getpriority` devuelve la prioridad de `process_id`. Como los niveles de prioridades cambian entre los tipos de sistemas y las versiones de kernel, lea la página de manual getpriority(2) de su sistema para detalles específicos.

## Parámetros

`process_id`  
Si `null`, se utiliza el identificador del proceso actual.

`mode`  
Una constante entre `PRIO_PGRP`, `PRIO_USER`, `PRIO_PROCESS`, `PRIO_DARWIN_BG` o `PRIO_DARWIN_THREAD`.

## Valores devueltos

`pcntl_getpriority` devuelve la prioridad del proceso o `false` en caso de error. Un valor numérico más pequeño hace que la planificación sea más favorable.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `process_id` es ahora nullable. |

## Véase también

`pcntl_setpriority`
