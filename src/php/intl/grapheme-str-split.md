---
title: grapheme_str_split
description: Divide una string en un array
source_url: https://www.php.net/manual/es/function.grapheme-str-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-str-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 122d5d096
order: 39830
---

grapheme_str_split

Divide una string en un array

## Descripción

```php
grapheme_str_split(string $string, [int $length]): array
```php

Esta función devuelve un array de strings, es una versión de `str_split` con soporte para caracteres de cluster de grafemas. Si el argumento `length` es especificado, la string es dividida en trozos de la longitud especificada en clusters de grafemas (no en bytes).

## Parámetros

`string`  
La `string` a dividir en clusters de grafemas o en trozos. `string` debe ser un UTF-8 válido.

`length`  
Cada elemento del array devuelto estará compuesto por `length` clusters de grafemas.

## Valores devueltos

`grapheme_str_split` devuelve un array de strings, o `false` si ocurre un error.

## Errores/Excepciones

Si `string` no es una string válida, se lanzará una `ValueError`.

## Véase también

str_split

mb_str_split

Segmentación de texto Unicode: Límites de Clusters de Grafemas
