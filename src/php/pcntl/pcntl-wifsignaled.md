---
title: pcntl_wifsignaled
description: Verifica si el código de estado representa una terminación debido a una
  señal
source_url: https://www.php.net/manual/es/function.pcntl-wifsignaled.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wifsignaled.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 96c9d88ba
order: 61480
---

pcntl_wifsignaled

Verifica si el código de estado representa una terminación debido a una señal

## Descripción

```php
pcntl_wifsignaled(int $status): bool
```php

Verifica si el proceso hijo termina porque una señal no pudo ser recibida.

## Parámetros

`status`  
El parámetro `status` es el parámetro status pasado a una llamada de `pcntl_waitpid` que tuvo éxito.

## Valores devueltos

Devuelve `true` si el proceso hijo termina porque una señal no pudo ser recibida, `false` en caso contrario.

## Véase también

`pcntl_waitpid`, `pcntl_signal`
