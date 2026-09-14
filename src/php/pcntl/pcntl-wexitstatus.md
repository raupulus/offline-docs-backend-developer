---
title: pcntl_wexitstatus
description: Devuelve el código de un proceso hijo terminado
source_url: https://www.php.net/manual/es/function.pcntl-wexitstatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wexitstatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: b890f28c0
order: 61450
---

pcntl_wexitstatus

Devuelve el código de un proceso hijo terminado

## Descripción

```php
pcntl_wexitstatus(int $status): int
```php

Devuelve el código de retorno del proceso hijo. Esta función solo es útil si la función `pcntl_wifexited` ha devuelto `true`.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve el código de retorno. Si la funcionalidad no es soportada por el sistema operativo, `false` es devuelto.

## Véase también

`pcntl_waitpid`, `pcntl_wifexited`
