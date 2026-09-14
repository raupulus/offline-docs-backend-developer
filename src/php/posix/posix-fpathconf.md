---
title: posix_fpathconf
description: Devuelve el valor de un límite configurable
source_url: https://www.php.net/manual/es/function.posix-fpathconf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-fpathconf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: 42ed815ea
order: 65140
---

posix_fpathconf

Devuelve el valor de un límite configurable

## Descripción

```php
posix_fpathconf(resource $file_descriptor, int $name): int
```php

Devuelve el valor de un límite configurable de `name` para `file_descriptor`.

## Parámetros

`file_descriptor`  
El descriptor de fichero, el cual se espera que sea un `resource` de fichero o un `int`. Se asumirá que un `int` es un descriptor de fichero que puede ser pasado directamente a la llamada al sistema subyacente.

`name`  
El nombre del límite configurable, uno de los siguientes. `POSIX_PC_LINK_MAX`, `POSIX_PC_MAX_CANON`, `POSIX_PC_MAX_INPUT`, `POSIX_PC_NAME_MAX`, `POSIX_PC_PATH_MAX`, `POSIX_PC_PIPE_BUF`, `POSIX_PC_CHOWN_RESTRICTED`, `POSIX_PC_NO_TRUNC`, `POSIX_PC_ALLOC_SIZE_MIN`, `POSIX_PC_SYMLINK_MAX`.

## Valores devueltos

Devuelve el límite configurable o `false`.

## Errores/Excepciones

Lanza una `ValueError` si `file_descriptor` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora establece `last_error` a `EBADF` y emite un `E_WARNING` cuando se encuentra un descriptor de archivo inválido. |

## Ejemplos

Ejemplo de `posix_fpathconf`

Este ejemplo devuelve la longitud máxima del nombre de ruta en bytes para el directorio actual.

```
<?php
$fd = fopen(__DIR__, "r");
echo posix_fpathconf($fd, POSIX_PC_PATH_MAX);
?>

   
```php

El ejemplo anterior mostrará:

    4096

## Véase también

posix_pathconf
