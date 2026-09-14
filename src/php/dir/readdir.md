---
title: readdir
description: Leer entrada desde el manejador de directorio
source_url: https://www.php.net/manual/es/function.readdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/readdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_revision: 5c7e9e135
order: 12060
---

readdir

Leer entrada desde el manejador de directorio

## Descripción

```php
readdir([resource $dir_handle]): string
```php

Devuelve el nombre de la siguiente entrada en el directorio. Las entradas se devuelven en el orden en que están almacenadas por el sistema de archivos.

## Parámetros

`dir_handle`  
Un manejador de directorio `resource` previamente abierto con `opendir`. Si `dir_handle` es `null` se utilizará el último manejador abierto usando `opendir`.

## Valores devueltos

Devuelve el nombre de la entrada en caso de éxito, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Usar `null` para `dir_handle` ahora está deprecado. En su lugar, debe proporcionarse explícitamente el último manejador de directorio abierto. |
| 8.0.0 | `dir_handle` ahora es nullable. |

## Ejemplos

Para un ejemplo completo, consulte la documentación de `opendir`.

## Véase también

opendir

rewinddir

closedir

dir

is_dir

glob

scandir
