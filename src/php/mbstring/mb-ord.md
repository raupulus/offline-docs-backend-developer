---
title: mb_ord
description: Obtiene el punto de código Unicode de un carácter
source_url: https://www.php.net/manual/es/function.mb-ord.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ord.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 62126c55f
order: 45300
---

mb_ord

Obtiene el punto de código Unicode de un carácter

## Descripción

```php
mb_ord(string $string, [string $encoding]): int
```php

Devuelve el punto de código Unicode para el carácter proporcionado.

Esta función complementa `mb_chr`.

## Parámetros

`string`  
Una cadena de caracteres

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

El punto de código Unicode para el primer carácter de `string` o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Ejemplos

Un ejemplo básico de `mb_ord`

```
<?php
var_dump(mb_ord("A", "UTF-8"));
var_dump(mb_ord("🐘", "UTF-8"));
var_dump(mb_ord("\x80", "ISO-8859-1"));
var_dump(mb_ord("\x80", "Windows-1252"));
?>

    
```php

El ejemplo anterior mostrará:

         int(65)
         int(128024)
         int(128)
         int(8364)

## Véase también

`mb_internal_encoding`, `mb_chr`, `IntlChar::ord`, `ord`
