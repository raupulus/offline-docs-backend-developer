---
title: fdf_get_value
description: Devuelve el valor de un campo FDF
source_url: https://www.php.net/manual/es/function.fdf-get-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-get-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22490
---

fdf_get_value

Devuelve el valor de un campo FDF

## Descripción

```php
fdf_get_value(resource $fdf_document, string $fieldname, [int $which]): mixed
```php

Devuelve el valor de un campo FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  
Nombre del campo FDF, en forma de `string`.

`which`  
Los elementos de un campo array pueden ser leídos proporcionando este argumento opcional, en forma de un entero cuyo valor mínimo será `0`. Para los campos que no son arrays, este argumento opcional será ignorado.

## Valores devueltos

Devuelve el valor del campo.

## Véase también

fdf_set_value
