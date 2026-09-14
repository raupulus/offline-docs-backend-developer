---
title: fdf_set_target_frame
description: Configura el marco de destino para la visualización del formulario
source_url: https://www.php.net/manual/es/function.fdf-set-target-frame.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-target-frame.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22670
---

fdf_set_target_frame

Configura el marco de destino para la visualización del formulario

## Descripción

```php
fdf_set_target_frame(resource $fdf_document, string $frame_name): bool
```php

Configura el marco de destino para la visualización del resultado PDF definido por `fdf_save_file`.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`frame_name`  
El nombre del marco, en forma de `string`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_save_file
