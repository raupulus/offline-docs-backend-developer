---
title: zip_entry_close
description: Cierra un directorio de archivo
source_url: https://www.php.net/manual/es/function.zip-entry-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/functions/zip-entry-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: true
translation_revision: 963af75fa
order: 108040
---

zip_entry_close

Cierra un directorio de archivo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] zip_entry_close(resource $zip_entry): bool
```php

`zip_entry_close` cierra un directorio de archivo dado.

## Parámetros

`zip_entry`  
Un directorio de archivo previamente abierto con la función `zip_entry_open`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está obsoleta en favor de la API orientada a objetos. |

## Véase también

`zip_entry_open`, `zip_entry_read`
