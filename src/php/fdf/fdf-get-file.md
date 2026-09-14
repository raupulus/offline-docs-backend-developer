---
title: fdf_get_file
description: Lee el valor de la clave /F
source_url: https://www.php.net/manual/es/function.fdf-get-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-get-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22450
---

fdf_get_file

Lee el valor de la clave /F

## Descripción

```php
fdf_get_file(resource $fdf_document): string
```php

Lee el valor de la clave `/F`.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

## Valores devueltos

Devuelve el valor de la clave, en forma de `string`.

## Véase también

fdf_set_file
