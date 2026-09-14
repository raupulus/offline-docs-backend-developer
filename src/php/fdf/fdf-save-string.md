---
title: fdf_save_string
description: Devuelve un documento FDF en forma de string
source_url: https://www.php.net/manual/es/function.fdf-save-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-save-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22560
---

fdf_save_string

Devuelve un documento FDF en forma de

string

## Descripción

```php
fdf_save_string(resource $fdf_document): string
```php

Devuelve un documento FDF en forma de `string`.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

## Valores devueltos

Devuelve el documento, en forma de `string`, o `false` en caso de error.

## Ejemplos

Leer un documento FDF en forma de `string`

```
<?php
$fdf = fdf_create();
fdf_set_value($fdf, "foo", "bar");
$str = fdf_save_string($fdf);
fdf_close($fdf);
echo $str;
?>

   
```php

El ejemplo anterior mostrará:

    %FDF-1.2
    %âãÏÓ
    1 0 obj
    <<
    /FDF << /Fields 2 0 R >>
    >>
    endobj
    2 0 obj
    [
    << /T (foo)/V (bar)>>
    ]
    endobj
    trailer
    <<
    /Root 1 0 R

    >>
    %%EOF

## Véase también

fdf_open_string

fdf_close

fdf_create

fdf_save
