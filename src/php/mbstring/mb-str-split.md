---
title: mb_str_split
description: Para una cadena multibyte dada, devuelve un array de sus caracteres
source_url: https://www.php.net/manual/es/function.mb-str-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-str-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: bb66ce4d4
order: 45410
---

mb_str_split

Para una cadena multibyte dada, devuelve un array de sus caracteres

## Descripción

```php
mb_str_split(string $string, [int $length], [string $encoding]): array
```php

Esta función devolverá un array de strings, es una versión de `str_split` con soporte para codificaciones de tamaño de carácter variable así como para codificaciones de tamaño fijo de caracteres de 1, 2 o 4 bytes. Si el parámetro `length` es especificado, la cadena se divide en bloques de la longitud especificada en caracteres (y no en bytes). El parámetro `encoding` es opcional pero se recomienda proporcionarlo.

## Parámetros

`string`  
El `string` a dividir en caracteres o en trozos.

`length`  
Si se especifica, cada elemento del array devuelto estará compuesto por múltiples caracteres en lugar de un solo carácter.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

Una cadena de caracteres que especifica uno de los [encodings soportados](#mbstring.supported-encodings).

## Valores devueltos

`mb_str_split` devuelve un array de strings.

## Historial de cambios

| Versión | Descripción                                           |
|---------|-------------------------------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`.                       |
| 8.0.0   | Esta función ya no devuelve `false` en caso de fallo. |

## Véase también

`str_split`, `grapheme_str_split`, `explode`
