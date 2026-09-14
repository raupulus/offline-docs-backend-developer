---
title: fdf_set_submit_form_action
description: Modifica la acción de un formulario
source_url: https://www.php.net/manual/es/function.fdf-set-submit-form-action.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-submit-form-action.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22660
---

fdf_set_submit_form_action

Modifica la acción de un formulario

## Descripción

```php
fdf_set_submit_form_action(resource $fdf_document, string $fieldname, int $trigger, string $script, int $flags): bool
```php

Modifica la acción de un formulario.

## Parámetros

`fdf_document`  
El gestor de documento, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  
Nombre del campo FDF, en forma de `string`.

`trigger`  

`script`  

`flags`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_set_javascript_action
