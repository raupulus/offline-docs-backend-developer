---
title: zip_open
description: Abre un archivo ZIP
source_url: https://www.php.net/manual/es/function.zip-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/functions/zip-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: true
translation_revision: 963af75fa
order: 108110
---

zip_open

Abre un archivo ZIP

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] zip_open(string $filename): resource
```php

`zip_open` abre un nuevo archivo ZIP para lectura.

## Parámetros

`filename`  
El nombre del archivo ZIP a abrir.

## Valores devueltos

Devuelve un recurso a utilizar más tarde con las funciones `zip_read` y `zip_close`, o bien devuelve `false` o el número de error si el parámetro `filename` no existe o en caso de otro error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está obsoleta en favor de la API orientada a objetos, ver ZipArchive::open. |

## Véase también

`zip_read`, `zip_close`
