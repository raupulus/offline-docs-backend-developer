---
title: mb_str_pad
description: Rellena una cadena multibyte hasta una cierta longitud con otra cadena
  multibyte
source_url: https://www.php.net/manual/es/function.mb-str-pad.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-str-pad.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: e4e09f45c
order: 45400
---

mb_str_pad

Rellena una cadena multibyte hasta una cierta longitud con otra cadena multibyte

## Descripción

```php
mb_str_pad(string $string, int $length, [string $pad_string], [int $pad_type], [string $encoding]): string
```php

Esta función devuelve el `string` rellenado por la izquierda, la derecha o ambos lados hasta la longitud de relleno especificada, donde la longitud se mide en puntos de código Unicode. Si el argumento opcional `pad_string` no se proporciona, el `string` se rellena con espacios, de lo contrario se rellena con caracteres de `pad_string` hasta el límite.

## Parámetros

`string`  
La cadena de entrada.

`length`  
Si el valor de `length` es negativo, inferior o igual a la longitud de la cadena de entrada, no se realiza ningún relleno y `string` será devuelto.

`pad_string`  
> [!NOTE]
> El `pad_string` puede ser truncado si el número requerido de caracteres de relleno no puede ser dividido equitativamente por la longitud del `pad_string`.

`pad_type`  
El argumento opcional `pad_type` puede ser `STR_PAD_RIGHT`, `STR_PAD_LEFT`, o `STR_PAD_BOTH`. Por omisión `STR_PAD_RIGHT`.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la cadena rellenada.

## Ejemplos

Ejemplo de `mb_str_pad`

```
<?php
var_dump(mb_str_pad('▶▶', 6, '❤❓❇', STR_PAD_RIGHT)); // string(18) "▶▶❤❓❇❤"
var_dump(mb_str_pad('▶▶', 6, '❤❓❇', STR_PAD_LEFT));  // string(18) "❤❓❇❤▶▶"
var_dump(mb_str_pad('▶▶', 6, '❤❓❇', STR_PAD_BOTH));  // string(18) "❤❓▶▶❤❓"

var_dump(mb_str_pad("🎉", 3, "祝", STR_PAD_LEFT));   // string(10) "祝祝🎉"
?>

    
```php
