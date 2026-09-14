---
title: pcntl_wifexited
description: Verifica si el código de retorno representa una finalización normal
source_url: https://www.php.net/manual/es/function.pcntl-wifexited.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wifexited.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 96c9d88ba
order: 61470
---

pcntl_wifexited

Verifica si el código de retorno representa una finalización normal

## Descripción

```php
pcntl_wifexited(int $status): bool
```php

Verifica si el código de estado del proceso hijo representa una finalización normal.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve `true` si el proceso hijo ha devuelto un código que representa una finalización normal, `false` en caso contrario.

## Véase también

`pcntl_waitpid`, `pcntl_wexitstatus`
