---
title: fdf_set_flags
description: Modifica una opción de un campo
source_url: https://www.php.net/manual/es/function.fdf-set-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-flags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22610
---

fdf_set_flags

Modifica una opción de un campo

## Descripción

```php
fdf_set_flags(resource $fdf_document, string $fieldname, int $whichFlags, int $newFlags): bool
```php

Modifica una opción de un campo.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  
Nombre del campo FDF, en forma de `string`.

`whichFlags`  

`newFlags`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_set_opt
