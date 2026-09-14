---
title: hebrev
description: Convierte un texto lógico hebreo en texto visual
source_url: https://www.php.net/manual/es/function.hebrev.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/hebrev.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 88750
---

hebrev

Convierte un texto lógico hebreo en texto visual

## Descripción

```php
hebrev(string $string, [int $max_chars_per_line]): string
```php

Convierte un texto lógico hebreo en texto visual.

La función intenta evitar la división de palabras.

## Parámetros

`string`  
Un string de entrada en hebreo.

`max_chars_per_line`  
El argumento opcional `max_chars_per_line` indica el número máximo de caracteres por línea en el resultado.

## Valores devueltos

Devuelve el string visual.

## Véase también

`hebrevc`
