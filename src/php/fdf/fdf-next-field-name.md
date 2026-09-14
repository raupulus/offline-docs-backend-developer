---
title: fdf_next_field_name
description: Lee el nombre del siguiente campo FDF
source_url: https://www.php.net/manual/es/function.fdf-next-field-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-next-field-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22520
---

fdf_next_field_name

Lee el nombre del siguiente campo FDF

## Descripción

```php
fdf_next_field_name(resource $fdf_document, [string $fieldname]): string
```php

Lee el nombre del siguiente campo FDF. Este nombre podrá ser utilizado en varias funciones.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  
Nombre del campo FDF, en forma de `string`. Si no se proporciona, se devolverá el primer campo.

## Valores devueltos

Devuelve el nombre del campo, en forma de `string`.

## Ejemplos

Detectar todos los nombres de un formulario FDF

```
<?php
$fdf = fdf_open($HTTP_FDF_DATA);
for ($field = fdf_next_field_name($fdf);
    $field != "";
    $field = fdf_next_field_name($fdf, $field)) {
    echo "campo: $field\n";
}
?>

   
```php

## Véase también

fdf_get_value
