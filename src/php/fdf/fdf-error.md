---
title: fdf_error
description: Devuelve el mensaje de error FDF
source_url: https://www.php.net/manual/es/function.fdf-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22410
---

fdf_error

Devuelve el mensaje de error FDF

## Descripción

```php
fdf_error([int $error_code]): string
```php

Devuelve el mensaje de error FDF.

## Parámetros

`error_code`  
Un código de error obtenido con la función `fdf_errno`. Si no se proporciona, esta función utiliza el código de error interno definido por la última operación.

## Valores devueltos

Devuelve el mensaje de error en forma de un `string` o la cadena `no error` si no hay ninguno.

## Véase también

fdf_errno
