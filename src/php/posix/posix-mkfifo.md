---
title: posix_mkfifo
description: Crear un archivo especial fifo (un pipe con nombre)
source_url: https://www.php.net/manual/es/function.posix-mkfifo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-mkfifo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65360
---

posix_mkfifo

Crear un archivo especial fifo (un pipe con nombre)

## Descripción

```php
posix_mkfifo(string $filename, int $permissions): bool
```php

`posix_mkfifo` crea un archivo `FIFO` especial que existe en el sistema de archivos y actúa como un punto de comunicación bi-direccional para los procesos.

## Parámetros

`filename`  
Ruta al archivo `FIFO`.

`permissions`  
El segundo parámetro `permissions` tiene que ser definido en notación octal (p.ej. 0644). El permiso del `FIFO` recién creado depende también del valor `umask` actual. Los permisos del archivo creado son (modo & ~umask).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
