---
title: filter_has_var
description: Verifica si una variable de un tipo específico existe
source_url: https://www.php.net/manual/es/function.filter-has-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-has-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: 627f933cf
order: 24170
---

filter_has_var

Verifica si una variable de un tipo específico existe

## Descripción

```php
filter_has_var(int $input_type, string $var_name): bool
```php

## Parámetros

`input_type`  
Una constante entre `INPUT_GET`, `INPUT_POST`, `INPUT_COOKIE`, `INPUT_SERVER` o `INPUT_ENV`.

`var_name`  
Nombre de la variable a verificar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
