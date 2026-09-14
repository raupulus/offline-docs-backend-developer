---
title: mb_encode_mimeheader
description: Codifica una cadena para un encabezado MIME
source_url: https://www.php.net/manual/es/function.mb-encode-mimeheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-encode-mimeheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 398329d3c
order: 45060
---

mb_encode_mimeheader

Codifica una cadena para un encabezado MIME

## Descripción

```php
mb_encode_mimeheader(string $string, [string $charset], [string $transfer_encoding], [string $newline], [int $indent]): string
```php

Codifica una `string` `string` dada en un encabezado MIME.

## Parámetros

`string`  
La `string` a codificar. Su codificación debería ser idéntica a `mb_internal_encoding`.

`charset`  
`charset` es el nombre de la codificación utilizada por la cadena `string`. El valor por omisión se determina mediante los parámetros actuales de NLS (`mbstring.language`).

`transfer_encoding`  
`transfer_encoding` es la codificación de transferencia. Puede ser `"B"` (Base64) o `"Q"` (Quoted-Printable). Por omisión, es `"B"`.

`newline`  
`newline` especifica los finales de línea (EOF: `end-of-line`) utilizados por `mb_encode_mimeheader` para formatear la cadena (una [RFC](https://datatracker.ietf.org/doc/html/rfc2822) define la longitud de una cadena a partir de la cual se debe añadir un final de línea. La longitud actual es 74 caracteres). El valor por omisión es `"\r\n"` (CRLF).

`indent`  
Indentación de la primera línea (número de caracteres en el encabezado antes de `string`).

## Valores devueltos

Una versión convertida de la `string` en ASCII.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Los octetos `NUL` (0) ya no se eliminan durante la codificación en Quoted-Printable, sino que se codifican como `=00`. |
| 8.0.0 | `charset` y `transfer_encoding` ahora son nulos. |

## Ejemplos

Ejemplo con `mb_encode_mimeheader`

```
<?php
$name = "太郎"; // kanji
$mbox = "kru";
$doma = "gtinn.mon";
$addr = '"' . addcslashes(mb_encode_mimeheader($name, "UTF-7", "Q"), '"') . '" <' . $mbox . "@" . $doma . ">";
echo $addr;
?>

    
```php

El ejemplo anterior mostrará:

    "=?UTF-7?Q?+WSqQzg-?=" <kru@gtinn.mon>

## Notas

> [!NOTE]
> Esta función no está diseñada para cortar líneas en medio de palabras. Este comportamiento puede añadir espacios no deseados en una palabra de la cadena original.

## Véase también

`mb_decode_mimeheader`
