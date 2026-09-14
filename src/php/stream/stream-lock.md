---
title: streamWrapper::stream_lock
description: Bloqueo de archivos asesorado
source_url: https://www.php.net/manual/es/streamwrapper.stream-lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 38231ac29
order: 88440
---

streamWrapper::stream_lock

Bloqueo de archivos asesorado

## Descripción

```php
public streamWrapper::stream_lock(int $operation): bool
```php

Este método es llamado en respuesta a `flock`, cuando se utiliza `file_put_contents` (cuando el parámetro `flags` contiene `LOCK_EX`), `stream_set_blocking` y cuando se cierra el flujo (`LOCK_UN`).

## Parámetros

`operation`  
`operation` es una de las operaciones siguientes:

- `LOCK_SH` para adquirir un bloqueo compartido (lectura).

- `LOCK_EX` para adquirir un bloqueo exclusivo (escritura).

- `LOCK_UN` para liberar un bloqueo (compartido o exclusivo).

También es posible añadir `LOCK_NB` como máscara de bits a una de las operaciones anteriores, si el bloqueo no debe bloquear durante el intento de bloqueo (no soportado en Windows).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un `E_WARNING` si la llamada a este método falla (es decir, no implementado).

## Véase también

`stream_set_blocking`, `flock`
