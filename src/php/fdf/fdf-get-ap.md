---
title: fdf_get_ap
description: Lee la apariencia de un campo
source_url: https://www.php.net/manual/es/function.fdf-get-ap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-get-ap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22420
---

fdf_get_ap

Lee la apariencia de un campo

## Descripción

```php
fdf_get_ap(resource $fdf_document, string $field, int $face, string $filename): bool
```php

Lee la apariencia del campo `field` (es decir, el valor de la clave /AP) y la almacena en el fichero `filename`.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`field`  

`face`  
Los valores posibles son `FDFNormalAP`, `FDFRolloverAP` y `FDFDownAP`.

`filename`  
La apariencia será almacenada en este parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
