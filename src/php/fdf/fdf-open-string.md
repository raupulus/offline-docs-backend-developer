---
title: fdf_open_string
description: Lee un documento FDF a partir de un string
source_url: https://www.php.net/manual/es/function.fdf-open-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-open-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22530
---

fdf_open_string

Lee un documento FDF a partir de un

string

## Descripción

```php
fdf_open_string(string $fdf_data): resource
```php

Lee un documento FDF a partir de un `string`.

Se puede utilizar `fdf_open_string` con la variable `$HTTP_FDF_DATA` para procesar datos de formularios provenientes de clientes remotos.

## Parámetros

`fdf_data`  
Los datos, como devueltos desde un formulario PDF o creados utilizando las funciones `fdf_create` y `fdf_save_string`.

## Valores devueltos

Devuelve un gestor de documento FDF, o `false` si ocurre un error.

## Ejemplos

Acceso a los datos de formulario FDF

```
<?php
$fdf = fdf_open_string($HTTP_FDF_DATA);
/* ... */
fdf_close($fdf);
?>

   
```php

## Véase también

fdf_open

fdf_close

fdf_create

fdf_save_string
