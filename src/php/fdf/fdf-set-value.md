---
title: fdf_set_value
description: Modifica el valor de un campo FDF
source_url: https://www.php.net/manual/es/function.fdf-set-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22680
---

fdf_set_value

Modifica el valor de un campo FDF

## Descripción

```php
fdf_set_value(resource $fdf_document, string $fieldname, mixed $value, [int $isName]): bool
```php

Modifica el valor de un campo FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  
Nombre del campo FDF, en forma de `string`.

`value`  
Este parámetro debe ser almacenado como un string incluso si es un array. En este caso, todos los elementos del array serán almacenados como un array de valores.

`isName`  
> [!NOTE]
> En versiones anteriores de la suite FDF, el último parámetro determinaba si el valor del campo debía ser convertido en un nombre PDF (`isname` = 1) o posicionado como un string (`isname` = 0).
>
> El valor ya no está en la suite actual, versión 5.0. Por razones de compatibilidad, esto sigue siendo soportado como un parámetro opcional, pero ignorado internamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_get_value

fdf_remove_item
