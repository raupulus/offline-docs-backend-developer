---
title: stream_set_read_buffer
description: Configura el buffer de lectura de un flujo
source_url: https://www.php.net/manual/es/function.stream-set-read-buffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-set-read-buffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 88090
---

stream_set_read_buffer

Configura el buffer de lectura de un flujo

## Descripción

```php
stream_set_read_buffer(resource $stream, int $size): int
```php

Configura el buffer de lectura de un flujo. Equivalente a `stream_set_write_buffer`, pero para operaciones de lectura.

## Parámetros

`stream`  
El puntero de fichero.

`size`  
El número de bytes a almacenar en el buffer. Si `size` es 0, las operaciones se realizan sin buffer. Esto garantiza que las operaciones con `fread` se completen antes de que otros procesos puedan leer en el flujo de salida.

## Valores devueltos

Devuelve 0 en caso de éxito, o otro valor si la petición falla.

## Véase también

stream_set_write_buffer
