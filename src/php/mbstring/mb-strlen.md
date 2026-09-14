---
title: mb_strlen
description: Devuelve la longitud de una cadena
source_url: https://www.php.net/manual/es/function.mb-strlen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strlen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 92f1b8b17
order: 45460
---

mb_strlen

Devuelve la longitud de una cadena

## Descripción

```php
mb_strlen(string $string, [string $encoding]): int
```php

Obtiene la longitud de la cadena proporcionada.

## Parámetros

`string`  
La cadena a analizar.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve el número de caracteres en la cadena `string`, con la codificación `encoding`. Un carácter multiocteto es entonces contado como 1.

## Errores/Excepciones

Si la codificación es desconocida, se genera un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Véase también

`mb_internal_encoding`, `grapheme_strlen`, `iconv_strlen`, `strlen`
