---
title: pcntl_setns
description: Reasocia el proceso llamante con un espacio de nombres de otro proceso
source_url: https://www.php.net/manual/es/function.pcntl-setns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-setns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: acb474ea9
order: 61310
---

pcntl_setns

Reasocia el proceso llamante con un espacio de nombres de otro proceso

## Descripción

```php
pcntl_setns([int $process_id], [int $nstype]): bool
```php

Reasocia el proceso llamante con un espacio de nombres de Linux del proceso especificado por `process_id`, usando un pidfd obtenido mediante `pidfd_open(2)` y `setns(2)`.

## Parámetros

`process_id`  
El identificador del proceso de destino a cuyo espacio de nombres unirse. Si es `null`, se utiliza el propio PID del proceso llamante.

`nstype`  
El tipo de espacio de nombres con el que reasociarse. Por defecto es `CLONE_NEWNET` (espacio de nombres de red). Los valores posibles incluyen `CLONE_NEWNET`, `CLONE_NEWIPC`, `CLONE_NEWUTS`, y otros.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

pcntl_unshare
