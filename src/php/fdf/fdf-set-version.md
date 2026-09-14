---
title: fdf_set_version
description: Modifica el número de versión del fichero FDF
source_url: https://www.php.net/manual/es/function.fdf-set-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22690
---

fdf_set_version

Modifica el número de versión del fichero FDF

## Descripción

```php
fdf_set_version(resource $fdf_document, string $version): bool
```php

Modifica el número de versión del documento FDF actual.

Algunas funcionalidades soportadas por esta extensión solo están disponibles para las nuevas versiones de FDF.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`version`  
El número de versión. Para el toolkit FDF actual, puede ser `1.2`, `1.3` o `1.4`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_get_version
