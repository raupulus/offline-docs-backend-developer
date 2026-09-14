---
title: hebrevc
description: Convierte un texto lógico hebreo en texto visual, con saltos de línea
source_url: https://www.php.net/manual/es/function.hebrevc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/hebrevc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: f112cc1ec
order: 88760
---

hebrevc

Convierte un texto lógico hebreo en texto visual, con saltos de línea

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
hebrevc(string $hebrew_text, [int $max_chars_per_line]): string
```php

`hebrevc` es similar a `hebrev` con la diferencia de que convierte los saltos de línea (\n) en `"<br>\n"`.

La función intenta evitar la división de palabras.

## Parámetros

`hebrew_text`  
Un string de entrada en hebreo.

`max_chars_per_line`  
El argumento opcional `max_chars_per_line` indica el número máximo de caracteres por línea en el resultado.

## Valores devueltos

Devuelve el string visual.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |
| 7.4.0   | Esta función está obsoleta.     |

## Véase también

`hebrev`
