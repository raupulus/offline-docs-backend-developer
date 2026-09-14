---
title: stream_get_line
description: Lee una línea en un flujo
source_url: https://www.php.net/manual/es/function.stream-get-line.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-get-line.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: c3067ab0a
order: 87970
---

stream_get_line

Lee una línea en un flujo

## Descripción

```php
stream_get_line(resource $stream, int $length, [string $ending]): string
```php

`stream_get_line` lee una línea en el recurso `handle`.

La lectura termina cuando se han leído `length` bytes, cuando se encuentra la cadena no vacía especificada por `ending` (pero *no se incluirá* en el valor devuelto), o si ocurre EOF: cualquiera de los tres que ocurra primero.

Esta función es casi idéntica a `fgets` excepto que permite usar un delimitador de línea diferente de los caracteres estándar `\n`, `\r` y `\r\n`, y *no devuelve* el delimitador en sí.

## Parámetros

`stream`  
Un `resource` válido de fichero.

`length`  
El número máximo de bytes a leer desde el gestor. Los valores negativos no están soportados. Cero (`0`) significa el tamaño de chunk de socket por defecto, es decir, `8192` bytes.

`ending`  
Un delimitador de cadena opcional.

## Valores devueltos

`stream_get_line` lee una línea de tamaño máximo `length` en el flujo `stream` o `false` si ocurre un error.

## Véase también

fread

fgets

fgetc
