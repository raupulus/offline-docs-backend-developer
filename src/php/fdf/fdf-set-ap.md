---
title: fdf_set_ap
description: Fija la apariencia de un campo FDF
source_url: https://www.php.net/manual/es/function.fdf-set-ap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-ap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 22580
---

fdf_set_ap

Fija la apariencia de un campo FDF

## Descripción

```php
fdf_set_ap(resource $fdf_document, string $field_name, int $face, string $filename, int $page_number): bool
```php

Fija la apariencia de un campo FDF (es decir, el valor de la clave `/AP`).

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`field_name`  

`face`  
Los valores posibles son: `FDFNormalAP`, `FDFRolloverAP` y `FDFDownAP`.

`filename`  

`page_number`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
