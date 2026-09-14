---
title: fdf_create
description: Crea un nuevo documento FDF
source_url: https://www.php.net/manual/es/function.fdf-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22380
---

fdf_create

Crea un nuevo documento FDF

## Descripción

```php
fdf_create(): resource
```php

Crea un nuevo documento FDF.

Esta función es necesaria para aquellos que desean prellenar los campos de un formulario en un fichero PDF.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un gestor de documento FDF, o `false` si ocurre un error.

## Ejemplos

Prellemar un formulario PDF

```
<?php
$outfdf = fdf_create();
fdf_set_value($outfdf, "volume", $volume, 0);

fdf_set_file($outfdf, "http:/testfdf/resultlabel.pdf");
fdf_save($outfdf, "outtest.fdf");
fdf_close($outfdf);
Header("Content-type: application/vnd.fdf");
$fp = fopen("outtest.fdf", "r");
fpassthru($fp);
unlink("outtest.fdf");
?>

   
```php

## Véase también

fdf_close

fdf_save

fdf_open
