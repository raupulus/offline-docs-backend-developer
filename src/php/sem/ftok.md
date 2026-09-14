---
title: ftok
description: Convierte una ruta y un identificador de proyecto en una clave System
  V IPC
source_url: https://www.php.net/manual/es/function.ftok.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/ftok.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73440
---

ftok

Convierte una ruta y un identificador de proyecto en una clave System V IPC

## Descripción

```php
ftok(string $filename, string $project_id): int
```php

Convierte el argumento `filename` de un fichero existente, y el identificador de proyecto `proj`, en un entero `integer` para ser utilizado con la función `shmop_open` y otras funciones System V IPC.

## Parámetros

`filename`  
Ruta hacia un fichero accesible.

`project_id`  
Identificador del proyecto. Debe ser un solo carácter.

## Valores devueltos

En caso de éxito, el valor devuelto será el valor de la clave creada, de lo contrario, se devolverá `-1`.

## Véase también

shmop_open

sem_get
