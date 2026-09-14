---
title: mb_strwidth
description: Devuelve el tamaño de una cadena
source_url: https://www.php.net/manual/es/function.mb-strwidth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strwidth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 64f2f1c70
order: 45550
---

mb_strwidth

Devuelve el tamaño de una cadena

## Descripción

```php
mb_strwidth(string $string, [string $encoding]): int
```php

Devuelve la anchura de `string` `string`, donde los caracteres de media anchura cuentan como `1`, y los caracteres de doble anchura cuentan como `2`. Ver <http://www.unicode.org/reports/tr11/> para más detalles sobre la anchura de caracteres asiáticos del este.

Los caracteres de doble anchura son: `U+1100`-`U+115F`, `U+11A3`-`U+11A7`, `U+11FA`-`U+11FF`, `U+2329`-`U+232A`, `U+2E80`-`U+2E99`, `U+2E9B`-`U+2EF3`, `U+2F00`-`U+2FD5`, `U+2FF0`-`U+2FFB`, `U+3000`-`U+303E`, `U+3041`-`U+3096`, `U+3099`-`U+30FF`, `U+3105`-`U+312D`, `U+3131`-`U+318E`, `U+3190`-`U+31BA`, `U+31C0`-`U+31E3`, `U+31F0`-`U+321E`, `U+3220`-`U+3247`, `U+3250`-`U+32FE`, `U+3300`-`U+4DBF`, `U+4E00`-`U+A48C`, `U+A490`-`U+A4C6`, `U+A960`-`U+A97C`, `U+AC00`-`U+D7A3`, `U+D7B0`-`U+D7C6`, `U+D7CB`-`U+D7FB`, `U+F900`-`U+FAFF`, `U+FE10`-`U+FE19`, `U+FE30`-`U+FE52`, `U+FE54`-`U+FE66`, `U+FE68`-`U+FE6B`, `U+FF01`-`U+FF60`, `U+FFE0`-`U+FFE6`, `U+1B000`-`U+1B001`, `U+1F200`-`U+1F202`, `U+1F210`-`U+1F23A`, `U+1F240`-`U+1F248`, `U+1F250`-`U+1F251`, `U+20000`-`U+2FFFD`, `U+30000`-`U+3FFFD`. Todos los demás caracteres son caracteres de media anchura.

## Parámetros

`string`  
La cadena a analizar.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

El tamaño de la `string` `string`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Ejemplos

Ejemplo `mb_strwidth`

```
<?php
var_dump(
    mb_strwidth('a'),       // LATIN SMALL LETTER A
    mb_strwidth("\u{ff41}") // FULLWIDTH LATIN SMALL LETTER A
);
?>

   
```php

El ejemplo anterior mostrará:

    int(1)
    int(2)

## Véase también

`mb_strimwidth`, `mb_internal_encoding`
