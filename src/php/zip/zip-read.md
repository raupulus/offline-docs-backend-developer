---
title: zip_read
description: Lee la siguiente entrada en un archivo ZIP
source_url: https://www.php.net/manual/es/function.zip-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/functions/zip-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: true
translation_revision: 963af75fa
order: 108120
---

zip_read

Lee la siguiente entrada en un archivo ZIP

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] zip_read(resource $zip): resource
```php

`zip_read` lee la siguiente entrada en un archivo ZIP.

## Parámetros

`zip`  
Un archivo ZIP previamente abierto con la función `zip_open`.

## Valores devueltos

Devuelve un recurso de entrada de directorio para usar más tarde con las funciones `zip_entry_...`, o `false` si no hay más entradas para leer, o un código de error si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está obsoleta en favor de la API orientada a objetos, ver ZipArchive::statIndex. |

## Véase también

`zip_open`, `zip_close`, `zip_entry_open`, `zip_entry_read`
