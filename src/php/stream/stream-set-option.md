---
title: streamWrapper::stream_set_option
description: Cambia las opciones del flujo
source_url: https://www.php.net/manual/es/streamwrapper.stream-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: de8e36659
order: 88490
---

streamWrapper::stream_set_option

Cambia las opciones del flujo

## Descripción

```php
public streamWrapper::stream_set_option(int $option, int $arg1, int $arg2): bool
```php

Este método es llamado para modificar las opciones del flujo.

## Parámetros

`option`  
Una de las constantes entre: `STREAM_OPTION_BLOCKING` (Este método es llamado en respuesta a `stream_set_blocking`), `STREAM_OPTION_READ_TIMEOUT` (Este método es llamado en respuesta a `stream_set_timeout`), `STREAM_OPTION_READ_BUFFER` (Este método es llamado en respuesta a `stream_set_read_buffer`), `STREAM_OPTION_WRITE_BUFFER` (Este método es llamado en respuesta a `stream_set_write_buffer`)

`arg1`  
Si `option` es `STREAM_OPTION_BLOCKING`: modo de bloqueo solicitado (1 significa bloqueante, 0 no bloqueante)., `STREAM_OPTION_READ_TIMEOUT`: el tiempo de espera en segundos., `STREAM_OPTION_READ_BUFFER`: el modo de buffer (`STREAM_BUFFER_NONE` o `STREAM_BUFFER_FULL`)., `STREAM_OPTION_WRITE_BUFFER`: el modo de buffer (`STREAM_BUFFER_NONE` o `STREAM_BUFFER_FULL`).

`arg2`  
Si `option` es `STREAM_OPTION_BLOCKING`: esta opción no está activa., `STREAM_OPTION_READ_TIMEOUT`: el tiempo de espera en microsegundos., `STREAM_OPTION_READ_BUFFER`: el tamaño del buffer solicitado., `STREAM_OPTION_WRITE_BUFFER`: el tamaño del buffer solicitado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si `option` no está implementada, `false` debe ser retornado.

## Véase también

`stream_set_blocking`, `stream_set_timeout`, `stream_set_write_buffer`
