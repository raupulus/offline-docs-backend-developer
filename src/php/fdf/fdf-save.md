---
title: fdf_save
description: Guarda un documento FDF
source_url: https://www.php.net/manual/es/function.fdf-save.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-save.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22570
---

fdf_save

Guarda un documento FDF

## Descripción

```php
fdf_save(resource $fdf_document, [string $filename]): bool
```php

Guarda un documento FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`filename`  
Si se proporciona, el FDF resultante será escrito en este parámetro. De lo contrario, esta función escribirá el FDF en la salida estándar de PHP.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_close

fdf_create

fdf_save_string
