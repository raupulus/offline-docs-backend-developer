---
title: stream_set_blocking
description: Configura el modo de bloqueo de un flujo
source_url: https://www.php.net/manual/es/function.stream-set-blocking.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-set-blocking.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: a94b25918
order: 88070
---

stream_set_blocking

Configura el modo de bloqueo de un flujo

## Descripción

```php
stream_set_blocking(resource $stream, bool $enable): bool
```php

`stream_set_blocking` configura el modo de bloqueo del flujo `stream`.

Esta función funciona para todos los flujos que soportan el modo no bloqueante (actualmente, los ficheros y los flujos de sockets).

## Parámetros

`stream`  
El flujo.

`enable`  
Si `enable` vale `false`, `stream` se configurará en modo no bloqueante, y si vale `true`, `stream` se configurará en modo bloqueante. Esta llamada afecta a las funciones tales como `fgets` y `fread` que leen en flujos. En modo no bloqueante, la función `fgets` se ejecuta justo después de su llamada, mientras que en modo bloqueante, esperará datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> Esta función no tiene efecto para los ficheros locales bajo Windows. El modo no bloqueante no está soportado bajo Windows.

## Véase también

stream_select
