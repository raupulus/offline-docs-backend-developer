---
title: posix_ttyname
description: Devuelve el nombre del dispositivo del terminal
source_url: https://www.php.net/manual/es/function.posix-ttyname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-ttyname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: 42ed815ea
order: 65490
---

posix_ttyname

Devuelve el nombre del dispositivo del terminal

## Descripción

```php
posix_ttyname(resource $file_descriptor): string
```php

Devuelve un `string` para la ruta absoluta del terminal actual que está abierto en el puntero de fichero `file_descriptor`.

## Parámetros

`file_descriptor`  
El descriptor de fichero, el cual se espera que sea un `resource` de fichero o un `int`. Se asumirá que un `int` es un descriptor de fichero que puede ser pasado directamente a la llamada al sistema subyacente.

## Valores devueltos

En caso de éxito, devuelve un `string` correspondiente a la ruta absoluta de `file_descriptor`. En caso de error, devuelve `false`.

## Errores/Excepciones

Para valores enteros inválidos de `file_descriptor`, se genera un error `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `last_error` ahora se establece a `EBADF` cuando se encuentra un `file_descriptor` inválido. |
| 8.3.0 | Ahora se generan errores de tipo `E_WARNING` para las coerciones de enteros siguiendo las semánticas habituales de coerción de tipo de PHP. |
| 8.3.0 | Para valores enteros inválidos de `file_descriptor`, ahora se genera un error `E_WARNING`. |

## Véase también

`posix_isatty`, `stream_isatty`
