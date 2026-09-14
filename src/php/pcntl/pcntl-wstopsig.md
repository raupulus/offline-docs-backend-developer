---
title: pcntl_wstopsig
description: Devuelve la señal que causó la detención del proceso hijo
source_url: https://www.php.net/manual/es/function.pcntl-wstopsig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wstopsig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: b890f28c0
order: 61500
---

pcntl_wstopsig

Devuelve la señal que causó la detención del proceso hijo

## Descripción

```php
pcntl_wstopsig(int $status): int
```php

Devuelve el número de la señal que causó la detención del proceso hijo. Esta función es útil únicamente si `pcntl_wifstopped` ha devuelto `true`.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve el número de la señal. Si la funcionalidad no es soportada por el sistema operativo, `false` es devuelto.

## Véase también

`pcntl_waitpid`, `pcntl_wifstopped`
