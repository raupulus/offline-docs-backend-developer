---
title: stream_supports_lock
description: Indica si el flujo soporta bloqueo
source_url: https://www.php.net/manual/es/function.stream-supports-lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-supports-lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: dd07341fa
order: 88210
---

stream_supports_lock

Indica si el flujo soporta bloqueo

## Descripción

```php
stream_supports_lock(resource $stream): bool
```php

Indica si el flujo soporta bloqueo a través de `flock`.

## Parámetros

`stream`  
El flujo a comprobar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`flock`
