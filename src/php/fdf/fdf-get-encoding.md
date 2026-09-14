---
title: fdf_get_encoding
description: Lee el valor de la clave /Encoding
source_url: https://www.php.net/manual/es/function.fdf-get-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-get-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22440
---

fdf_get_encoding

Lee el valor de la clave /Encoding

## Descripción

```php
fdf_get_encoding(resource $fdf_document): string
```php

Recupera el valor de la clave `/Encoding`.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

## Valores devueltos

Devuelve la codificación, en forma de un `string`. Una cadena vacía es devuelta si el esquema `PDFDocEncoding/Unicode` es utilizado.

## Véase también

fdf_set_encoding
