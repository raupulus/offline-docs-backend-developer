---
title: zip_entry_read
description: Lee el contenido de un archivo en un directorio
source_url: https://www.php.net/manual/es/function.zip-entry-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/functions/zip-entry-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: true
translation_revision: 963af75fa
order: 108100
---

zip_entry_read

Lee el contenido de un archivo en un directorio

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] zip_entry_read(resource $zip_entry, [int $len]): string
```php

`zip_entry_read` lee en un directorio de archivo abierto.

## Parámetros

`zip_entry`  
Un directorio de archivo devuelto por la función `zip_read`.

`len`  
El número de bytes a devolver.

> [!NOTE]
> Esto debe ser el tamaño descomprimido que desea leer.

## Valores devueltos

Devuelve los datos leídos, una cadena vacía si se está al final del archivo, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está obsoleta en favor de la API orientada a objetos, ver ZipArchive::getFromIndex. |

## Véase también

`zip_entry_open`, `zip_entry_close`, `zip_entry_filesize`
