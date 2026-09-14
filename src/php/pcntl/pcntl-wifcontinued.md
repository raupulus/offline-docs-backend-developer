---
title: pcntl_wifcontinued
description: Comprueba si el proceso hijo ha continuado tras una parada de control
  de tareas
source_url: https://www.php.net/manual/es/function.pcntl-wifcontinued.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wifcontinued.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: acb474ea9
order: 61460
---

pcntl_wifcontinued

Comprueba si el proceso hijo ha continuado tras una parada de control de tareas

## Descripción

```php
pcntl_wifcontinued(int $status): bool
```php

Comprueba si el proceso hijo que provocó el retorno de `pcntl_waitpid` ha continuado tras una parada de control de tareas. Esta función solo es útil si la llamada a `pcntl_waitpid` se realizó usando la opción `WCONTINUED`.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve `true` si el proceso hijo que provocó el retorno de `pcntl_waitpid` ha continuado tras una parada de control de tareas, `false` en caso contrario.

## Véase también

pcntl_waitpid

pcntl_wifstopped

pcntl_wifexited

pcntl_wifsignaled
