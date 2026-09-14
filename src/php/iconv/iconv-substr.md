---
title: iconv_substr
description: Extrae una parte de una cadena
source_url: https://www.php.net/manual/es/function.iconv-substr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-substr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31250
---

iconv_substr

Extrae una parte de una cadena

## Descripción

```php
iconv_substr(string $string, int $offset, [int $length], [string $encoding]): string
```php

Extrae una parte de la cadena `string` a partir de la posición `offset` y con una longitud de `length`.

## Parámetros

`string`  
La `string` original.

`offset`  
Si `offset` no es negativo, `iconv_substr` devuelve el segmento de `string` comenzando en el carácter número `offset`, contando desde cero.

Si `offset` es negativo, `iconv_substr` devuelve el segmento comenzando en la posición `offset` caracteres desde el final de la `string` `string`.

`length`  
Si el parámetro `length` se proporciona y es positivo, el valor devuelto contendrá como máximo `length` caracteres de la porción de cadena que comienza en `offset` (dependiendo del tamaño de la cadena `string`).

Si `length` se proporciona y es negativo, `iconv_substr` extrae la porción externa de `string` desde el carácter número `offset` hasta el carácter número `length`, contando desde el final de la `string`. En el caso de que `offset` también sea negativo, la posición de inicio se calcula hacia atrás, siguiendo la regla explicada anteriormente.

`encoding`  
Si `encoding` se omite o es `null`, `string` se asume que está codificada en [iconv.internal_encoding](#iconv.configuration).

Tenga en cuenta que `offset` y `length` siempre se consideran como posiciones calculadas sobre la representación ASCII de los caracteres determinados por `encoding`, a diferencia de `substr` que se basa siempre en la posición por byte.

## Valores devueltos

Devuelve la porción de `string` especificada por los parámetros `offset` y `length`.

Si `string` es más pequeño que `offset`, se devolverá `false`. Si `string` tiene exactamente `offset` caracteres de longitud, se devolverá una `string` vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `length` y `encoding` ahora son nullable. |
| 7.0.11 | Si `string` tiene exactamente `offset` caracteres de longitud, se devolverá una cadena vacía. Antes de esta versión, se devolvía `false` en este caso. |

## Véase también

`substr`, `mb_substr`, `mb_strcut`
