---
title: pcntl_wifstopped
description: Devuelve true si el proceso hijo está detenido
source_url: https://www.php.net/manual/es/function.pcntl-wifstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wifstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 61374bbe2
order: 61490
---

pcntl_wifstopped

Devuelve true si el proceso hijo está detenido

## Descripción

```php
pcntl_wifstopped(int $status): bool
```php

Devuelve true si el proceso hijo está detenido; esto solo es posible si la llamada a `pcntl_waitpid` se ha realizado con la opción `WUNTRACED`.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve `true` si el proceso hijo está detenido, `false` en caso contrario.

## Véase también

`pcntl_waitpid`
