---
title: fdf_open
description: Abre un documento FDF
source_url: https://www.php.net/manual/es/function.fdf-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22540
---

fdf_open

Abre un documento FDF

## Descripción

```php
fdf_open(string $filename): resource
```php

Abre un documento FDF.

Asimismo, se puede utilizar la función `fdf_open_string` para procesar el resultado de un formulario PDF enviado mediante un método POST.

## Parámetros

`filename`  
Ruta hacia el fichero FDF. Este fichero debe contener los datos tal como son devueltos por un formulario PDF o creados utilizando las funciones `fdf_create` y `fdf_save`.

## Valores devueltos

Devuelve un gestor de documento FDF, o `false` en caso de error.

## Ejemplos

Acceder a los datos del formulario

```
<?php
// Guarda el fichero FDF en un fichero temporal.
$fdffp = fopen("test.fdf", "w");
fwrite($fdffp, $HTTP_FDF_DATA, strlen($HTTP_FDF_DATA));
fclose($fdffp);

// Abre el fichero temporal y utiliza los datos.
$fdf = fdf_open("test.fdf");
/* ... */
fdf_close($fdf);
?>

   
```php

## Véase también

fdf_open_string

fdf_close

fdf_create

fdf_save
