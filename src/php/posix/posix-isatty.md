---
title: posix_isatty
description: Determina si un puntero de fichero es un terminal interactivo
source_url: https://www.php.net/manual/es/function.posix-isatty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-isatty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: 42ed815ea
order: 65340
---

posix_isatty

Determina si un puntero de fichero es un terminal interactivo

## Descripción

```php
posix_isatty(resource $file_descriptor): bool
```php

Determina si el puntero de fichero `file_descriptor` se refiere a un tipo de terminal de dispositivo válido.

## Parámetros

`file_descriptor`  
El descriptor de fichero, el cual se espera que sea un `resource` de fichero o un `int`. Se asumirá que un `int` es un descriptor de fichero que puede ser pasado directamente a la llamada al sistema subyacente.

## Valores devueltos

Devuelve `true` si `file_descriptor` es un puntero de fichero conectado a un terminal, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora emite un `E_WARNING` cuando se encuentra un `file_descriptor` inválido. |
| 8.4.0 | Define errno (número de error) a `EBADF` cuando el descriptor de fichero/flujo pasado es inválido. |
| 8.3.0 | Se generan ahora errores de tipo `E_WARNING` para las coerciones de enteros siguiendo las semánticas habituales de coerción de tipo de PHP. |

## Véase también

`posix_ttyname`, `stream_isatty`
