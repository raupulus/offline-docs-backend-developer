---
title: mb_convert_encoding
description: Convertir una cadena de un codificación de caracteres a otra
source_url: https://www.php.net/manual/es/function.mb-convert-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-convert-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 44990
---

mb_convert_encoding

Convertir una cadena de un codificación de caracteres a otra

## Descripción

```php
mb_convert_encoding(array $string, string $to_encoding, [array $from_encoding]): array
```php

Convierte la `string` desde `from_encoding`, o la codificación interna actual, a `to_encoding`. Opcionalmente desde `from_encoding`. Si `string` es un `array`, todos sus valores `string` serán convertidos recursivamente.

## Parámetros

`string`  
La `string` o `array` a convertir.

`to_encoding`  
La codificación deseada del resultado.

`from_encoding`  
La codificación actual utilizada para interpretar la `string`. Múltiples codificaciones pueden ser especificadas en forma de array (`array`) o lista separada por comas. En este caso, la codificación correcta será adivinada utilizando el mismo algoritmo que `mb_detect_encoding`.

Si `from_encoding` es omitido o `null`, el parámetro [mbstring.internal_encoding](#ini.mbstring.internal-encoding) será utilizado si está definido, de lo contrario el parámetro [default_charset](#ini.default-charset) será utilizado.

Ver [codificaciones soportadas](#mbstring.supported-encodings) para los valores válidos de `to_encoding` y `from_encoding`.

## Valores devueltos

La `string` o `array` codificado en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

A partir de PHP 8.0.0, una `ValueError` es lanzada si la valor de `to_encoding` o `from_encoding` es una codificación inválida. Anterior a PHP 8.0.0, una `E_WARNING` era emitida en su lugar.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | `mb_convert_encoding` ya no devolverá las siguientes codificaciones no textuales: `"Base64"`, `"QPrint"`, `"UUencode"`, `"HTML entities"`, `"7 bit"` y `"8 bit"`. |
| 8.0.0 | `mb_convert_encoding` lanzará ahora una `ValueError` cuando `to_encoding` es pasado una codificación inválida. |
| 8.0.0 | `mb_convert_encoding` lanzará ahora una `ValueError` cuando `from_encoding` es pasado una codificación inválida. |
| 8.0.0 | `from_encoding` ahora es nullable. |
| 7.2.0 | Esta función ahora acepta un `array` como `string`. Anteriormente, solo las `string` eran soportadas. |

## Ejemplos

Ejemplo con `mb_convert_encoding`

```
<?php
/* Convierte la codificación interna a SJIS */
$str = mb_convert_encoding($str, "SJIS");

/* Convierte EUC-JP a UTF-7 */
$str = mb_convert_encoding($str, "UTF-7", "EUC-JP");

/* Detecta automáticamente una codificación entre JIS, eucjp-win o sjis-win,
   Luego convierte a UCS-2LE */
$str = mb_convert_encoding($str, "UCS-2LE", "JIS, eucjp-win, sjis-win");

/* Si mbstring.language es "Japanese", "auto" es extendido a "ASCII,JIS,UTF-8,EUC-JP,SJIS" */
$str = mb_convert_encoding($str, "EUC-JP", "auto");
?>

    
```php

## Véase también

`mb_detect_order`, UConverter::transcode, `iconv`
