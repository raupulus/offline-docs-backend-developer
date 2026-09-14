---
title: iconv_strlen
description: Devuelve el número de caracteres de una cadena
source_url: https://www.php.net/manual/es/function.iconv-strlen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv-strlen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: 66eabb01b
order: 31220
---

iconv_strlen

Devuelve el número de caracteres de una cadena

## Descripción

```php
iconv_strlen(string $string, [string $encoding]): int
```php

A diferencia de `strlen`, el valor devuelto por `iconv_strlen` es el número de caracteres que forman parte de la secuencia de bytes `string`, lo cual no siempre coincide con el tamaño en bytes de la cadena de caracteres.

## Parámetros

`string`  
La `string`.

`encoding`  
Si `encoding` es omitido o `null`, `string` se asume que está codificada en [iconv.internal_encoding](#iconv.configuration).

## Valores devueltos

Devuelve el número de caracteres de la cadena `string`, en forma de `int`, o `false` si ocurre un error durante la codificación.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `encoding` ahora es nullable. |

## Véase también

`grapheme_strlen`, `mb_strlen`, `strlen`
