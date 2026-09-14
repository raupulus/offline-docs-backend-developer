---
title: fdf_set_encoding
description: Modifica la codificación de caracteres
source_url: https://www.php.net/manual/es/function.fdf-set-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22590
---

fdf_set_encoding

Modifica la codificación de caracteres

## Descripción

```php
fdf_set_encoding(resource $fdf_document, string $encoding): bool
```php

Modifica la codificación de caracteres del documento FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`encoding`  
El nombre de la codificación. Los siguientes valores son soportados: "`Shift-JIS`", "`UHC`", "`GBK`" y "`BigFive`".

Un `string` vacío reemplaza el valor por omisión de la codificación al esquema `PDFDocEncoding/Unicode`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
