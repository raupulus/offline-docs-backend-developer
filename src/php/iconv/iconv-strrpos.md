---
title: iconv_strrpos
description: Encuentra la posición de la última ocurrencia de un elemento en una cadena
source_url: https://www.php.net/manual/es/function.iconv-strrpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-strrpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: ab9a7d2e3
order: 31240
---

iconv_strrpos

Encuentra la posición de la última ocurrencia de un elemento en una cadena

## Descripción

```php
iconv_strrpos(string $haystack, string $needle, [string $encoding]): int
```php

Encuentra la última ocurrencia de `needle` en `haystack`.

A diferencia de la función `strpos`, el valor devuelto por `iconv_strrpos` es el número de caracteres antes de `needle`, en lugar de la posición en bytes de `needle`. Los caracteres son contados basándose en el juego de caracteres `charset`. Los caracteres son contados sobre la base del juego de caracteres `encoding` especificado.

## Parámetros

`haystack`  
La `string` completa.

`needle`  
La `string` buscada.

`encoding`  
Si el parámetro opcional `encoding` es omitido o `null`, `string` se asume que está codificado en [iconv.internal_encoding](#iconv.configuration).

Si `haystack` o `needle` no son strings, serán convertidos a string y reconocidos como código ASCII de cada carácter.

## Valores devueltos

Devuelve la posición numérica de la última ocurrencia de `needle` en `haystack`.

Si `needle` no es encontrado, `iconv_strrpos` devolverá `false`.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `encoding` ahora es nullable. |

## Véase también

`strrpos`, `iconv_strpos`, `mb_strrpos`
