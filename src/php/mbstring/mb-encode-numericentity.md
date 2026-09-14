---
title: mb_encode_numericentity
description: Codifica caracteres a referencia numérica HTML
source_url: https://www.php.net/manual/es/function.mb-encode-numericentity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-encode-numericentity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: a60ef6523
order: 45070
---

mb_encode_numericentity

Codifica caracteres a referencia numérica HTML

## Descripción

```php
mb_encode_numericentity(string $string, array $map, [string $encoding], [bool $hex]): string
```php

Convierte los códigos de caracteres especificados en `string` `string` de código de caracteres a referencia numérica de caracteres HTML.

## Parámetros

`string`  
El `string` que se está codificando.

`map`  
`map` es un array que especifica el área de código a convertir.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

`hex`  
Si la referencia de entidad devuelta debe estar en notación hexadecimal (de lo contrario, está en notación decimal).

## Valores devueltos

El `string` convertido.

## Errores/Excepciones

Lanza una ValueError si `map` no es una lista de `int`s.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `mb_encode_numericentity` ahora lanza una ValueError si `map` no es una lista de `int`s. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Ejemplos

`map` ejemplo

```
<?php
$convmap = array (
 int start_code1, int end_code1, int offset1, int mask1,
 int start_code2, int end_code2, int offset2, int mask2,
 ........
 int start_codeN, int end_codeN, int offsetN, int maskN );
// Especificar valor Unicode para start_codeN y end_codeN
// Añadir offsetN al valor y hacer un 'AND' a nivel de bits con maskN, luego
// convierte el valor a referencia numérica de string.
?>

    
```php

`mb_encode_numericentity` ejemplo

```
<?php

$str = "aAæÆあア𩸽";

/* Convertir todos los caracteres UTF8 hasta 4 bytes a referencia numérica de caracteres HTML */
$convmap = [0, 0x1FFFFF, 0, 0x10FFFF];
var_dump(mb_encode_numericentity($str, $convmap, "utf8"));

/* Convertir solo los caracteres UTF8 de 2 bytes y 4 bytes a referencia numérica de caracteres HTML */
$convmap = [
    0x80, 0x7FF, 0, 0x10FFFF,
    0x10000, 0x1FFFFF, 0, 0x10FFFF,
];
var_dump(mb_encode_numericentity($str, $convmap, "utf8"));
?>

    
```php

El ejemplo anterior mostrará:

    string(46) "&#97;&#65;&#230;&#198;&#12354;&#12450;&#40509;"
    string(28) "aA&#230;&#198;あア&#40509;"

## Véase también

`mb_decode_numericentity`
