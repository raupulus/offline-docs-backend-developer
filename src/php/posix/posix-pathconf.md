---
title: posix_pathconf
description: Devuelve el valor de un límite configurable
source_url: https://www.php.net/manual/es/function.posix-pathconf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-pathconf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: 8d417bd83
order: 65380
---

posix_pathconf

Devuelve el valor de un límite configurable

## Descripción

```php
posix_pathconf(string $path, int $name): int
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve el valor de un límite configurable de `name` para un `path`.

## Parámetros

`path`  
El nombre del fichero del que se desea obtener el límite.

`name`  
El nombre del límite configurable, uno de los siguientes. `POSIX_PC_LINK_MAX`, `POSIX_PC_MAX_CANON`, `POSIX_PC_MAX_INPUT`, `POSIX_PC_NAME_MAX`, `POSIX_PC_PATH_MAX`, `POSIX_PC_PIPE_BUF`, `POSIX_PC_CHOWN_RESTRICTED`, `POSIX_PC_NO_TRUNC`, `POSIX_PC_ALLOC_SIZE_MIN`, `POSIX_PC_SYMLINK_MAX`.

## Valores devueltos

Devuelve el límite configurable o `false`.

## Errores/Excepciones

Lanza una `ValueError` si `path` está vacío.

## Ejemplos

Ejemplo de `posix_pathconf`

Este ejemplo obtendrá la longitud máxima del nombre de ruta en bytes para el directorio temporal.

```
<?php
echo posix_pathconf(sys_get_temp_dir(), POSIX_PC_PATH_MAX);
?>

   
```php

El ejemplo anterior mostrará:

    4096

## Véase también

posix_fpathconf
