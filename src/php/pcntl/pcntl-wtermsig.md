---
title: pcntl_wtermsig
description: Devuelve la señal que causó el término del proceso hijo
source_url: https://www.php.net/manual/es/function.pcntl-wtermsig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wtermsig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: b890f28c0
order: 61510
---

pcntl_wtermsig

Devuelve la señal que causó el término del proceso hijo

## Descripción

```php
pcntl_wtermsig(int $status): int
```php

Devuelve el número de la señal que causó el término del proceso hijo. Esta función es útil solo si `pcntl_wifsignaled` devuelve `true`.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve el número de la señal. Si la funcionalidad no es soportada por el sistema operativo, `false` es devuelto.

## Véase también

`pcntl_waitpid`, `pcntl_signal`, `pcntl_wifsignaled`
