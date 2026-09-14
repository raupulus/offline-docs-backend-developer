---
title: iconv_strpos
description: Encuentra la posición de la primera ocurrencia de una cadena en otra
source_url: https://www.php.net/manual/es/function.iconv-strpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-strpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31230
---

iconv_strpos

Encuentra la posición de la primera ocurrencia de una cadena en otra

## Descripción

```php
iconv_strpos(string $haystack, string $needle, [int $offset], [string $encoding]): int
```php

Encuentra la posición de la primera ocurrencia de `needle` en `haystack`.

A diferencia de `strpos`, el valor devuelto por `iconv_strpos` es el número de caracteres que se encuentran antes de `needle`, en lugar de la posición en bytes donde `needle` fue encontrado. Los caracteres son contados basándose en el juego de caracteres especificado por `encoding`.

## Parámetros

`haystack`  
El `string` completo.

`needle`  
El `string` a buscar.

`offset`  
El parámetro opcional `offset` especifica la posición desde la cual debe comenzar la búsqueda. Si la posición es negativa, se cuenta desde el final del `string`.

`encoding`  
Si el parámetro `encoding` es omitido o `null`, `string` será codificado de acuerdo con [iconv.internal_encoding](#iconv.configuration).

Si `haystack` o `needle` no son strings, son convertidos a enteros y aplicados como valor ordinal de un carácter.

## Valores devueltos

Devuelve la posición numérica de la primera ocurrencia de `needle` en `haystack`.

Si `needle` no es encontrado, `iconv_strpos` devolverá `false`.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción                                 |
|---------|---------------------------------------------|
| 8.0.0   | `encoding` ahora es nullable.               |
| 7.1.0   | Se añadió soporte para `offset`s negativos. |

## Véase también

`strpos`, `iconv_strrpos`, `mb_strpos`
