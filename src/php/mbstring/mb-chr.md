---
title: mb_chr
description: Devuelve un carácter por su valor de punto de código Unicode
source_url: https://www.php.net/manual/es/function.mb-chr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-chr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 30c25e7d4
order: 44970
---

mb_chr

Devuelve un carácter por su valor de punto de código Unicode

## Descripción

```php
mb_chr(int $codepoint, [string $encoding]): string
```php

Devuelve una cadena que contiene el carácter especificado por el valor del punto de código Unicode, codificado en la codificación especificada.

Esta función complementa a `mb_ord`.

## Parámetros

`codepoint`  
Un valor de punto de código Unicode, p. ej. `128024` para *U+1F418 ELEPHANT*

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Una cadena que contiene el carácter solicitado, si puede ser representado en la codificación especificada o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
$values = [65, 63, 0x20AC, 128024];
foreach ($values as $value) {
    var_dump(mb_chr($value, 'UTF-8'));
    var_dump(mb_chr($value, 'ISO-8859-1'));
}
?>

   
```php

El ejemplo anterior mostrará:

        
    string(1) "A"
    string(1) "A"
    string(1) "?"
    string(1) "?"
    string(3) "€"
    bool(false)
    string(4) "🐘"
    bool(false)

## Véase también

`mb_internal_encoding`, `mb_ord`, `IntlChar::ord`, `chr`
