---
title: fdf_set_javascript_action
description: Modifica la acción javascript de un campo
source_url: https://www.php.net/manual/es/function.fdf-set-javascript-action.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-set-javascript-action.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: f86fd7b1c
order: 22620
---

fdf_set_javascript_action

Modifica la acción javascript de un campo

## Descripción

```php
fdf_set_javascript_action(resource $fdf_document, string $fieldname, int $trigger, string $script): bool
```php

Modifica la acción javascript de un campo dado.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  
Nombre del campo FDF, en forma de `string`.

`trigger`  

`script`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fdf_set_submit_form_action
