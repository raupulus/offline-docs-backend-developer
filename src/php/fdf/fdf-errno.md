---
title: fdf_errno
description: Devuelve el código de error de la última operación FDF
source_url: https://www.php.net/manual/es/function.fdf-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 22400
---

fdf_errno

Devuelve el código de error de la última operación FDF

## Descripción

```php
fdf_errno(): int
```php

Recupera el código de error de la última operación FDF.

Un mensaje de error es accesible a través de la función `fdf_error`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código de error en forma de `int` o `0` si no ha ocurrido ningún error.

## Véase también

fdf_error
