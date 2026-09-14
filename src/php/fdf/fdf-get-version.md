---
title: fdf_get_version
description: Lee el número de versión de la API FDF
source_url: https://www.php.net/manual/es/function.fdf-get-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-get-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22500
---

fdf_get_version

Lee el número de versión de la API FDF

## Descripción

```php
fdf_get_version([resource $fdf_document]): string
```php

Devuelve el número de versión FDF para el documento `fdf_document`, para la API si no se proporciona ningún argumento.

## Parámetros

`fdf_document`  
El gestor de documento, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

## Valores devueltos

Devuelve la versión, en forma de `string`. Para la versión actual del FDF toolkit 5.0, el número de versión es `5.0` y el número de versión del documento es `1.2`, `1.3` o `1.4`.

## Véase también

fdf_set_version
