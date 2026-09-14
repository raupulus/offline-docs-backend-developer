---
title: rewinddir
description: Reinicia el gestor de directorio
source_url: https://www.php.net/manual/es/function.rewinddir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/rewinddir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_revision: 5c7e9e135
order: 12070
---

rewinddir

Reinicia el gestor de directorio

## Descripción

```php
rewinddir([resource $dir_handle]): void
```php

Reinicia el flujo de directorio indicado por `dir_handle` al principio del directorio.

## Parámetros

`dir_handle`  
Un gestor de directorio `resource` previamente abierto con `opendir`. Si `dir_handle` es `null` se utilizará el último gestor abierto usando `opendir`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Usar `null` para `dir_handle` ahora está obsoleto. En su lugar, debe proporcionarse explícitamente el último gestor de directorio abierto. |
| 8.0.0 | `dir_handle` ahora es nullable. |

## Ejemplos

Para un ejemplo completo, consulte la documentación de `opendir`.

## Véase también

opendir

readdir

closedir

dir

is_dir

glob

scandir
