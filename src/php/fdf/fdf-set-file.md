---
title: fdf_set_file
description: Crea un documento PDF para mostrar datos FDF
source_url: https://www.php.net/manual/es/function.fdf-set-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 22600
---

fdf_set_file

Crea un documento PDF para mostrar datos FDF

## Descripción

```php
fdf_set_file(resource $fdf_document, string $url, [string $target_frame]): bool
```php

Crea un documento PDF para mostrar datos FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`url`  
Debe ser proporcionado en forma de URL absoluta.

`target_frame`  
Utilice este parámetro para especificar la frame en la que se mostrará el documento. También es posible definir el valor por omisión de este parámetro utilizando la función `fdf_set_target_frame`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Pasar datos FDF a un segundo formulario

```
<?php
/* Configura el encabezado para Adobe FDF */
fdf_header();

/* Inicia un nuevo fichero FDF */
$fdf = fdf_create();

/* Asigna al campo "foo" el valor de "bar" */
fdf_set_value($fdf, "foo", "bar");

/* Indica al cliente que muestre los datos FDF con "fdf_form.pdf" */
fdf_set_file($fdf, "http://www.example.com/fdf_form.pdf");

/* Muestra el FDF */
fdf_save($fdf);

/* Limpia */
fdf_close($fdf);
?>

   
```php

## Véase también

fdf_get_file

fdf_set_target_frame
