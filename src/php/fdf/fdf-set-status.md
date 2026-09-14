---
title: fdf_set_status
description: Establece el valor de la clave /STATUS
source_url: https://www.php.net/manual/es/function.fdf-set-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22650
---

fdf_set_status

Establece el valor de la clave /STATUS

## Descripción

```php
fdf_set_status(resource $fdf_document, string $status): bool
```php

Establece el valor de la clave `/STATUS`. Cuando un cliente recibe un FDF con un estado establecido, su valor se presentará en una caja de alerta.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`status`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_get_status
