---
title: zip_entry_compressionmethod
description: Lee el método de compresión usado en un directorio de archivo
source_url: https://www.php.net/manual/es/function.zip-entry-compressionmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/functions/zip-entry-compressionmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: true
translation_revision: 963af75fa
order: 108060
---

zip_entry_compressionmethod

Lee el método de compresión usado en un directorio de archivo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] zip_entry_compressionmethod(resource $zip_entry): string
```php

`zip_entry_compressionmethod` devuelve el método de compresión usado en el directorio de archivo especificado por `zip_entry`.

## Parámetros

`zip_entry`  
Un directorio de archivo devuelto por la función `zip_read`.

## Valores devueltos

El método de compresión, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está obsoleta en favor de la API orientada a objetos, ver ZipArchive::statIndex. |

## Véase también

`zip_open`, `zip_read`
