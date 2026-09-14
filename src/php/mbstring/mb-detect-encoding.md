---
title: mb_detect_encoding
description: Detectar la codificación de caracteres
source_url: https://www.php.net/manual/es/function.mb-detect-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-detect-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 7c4b5fb40
order: 45040
---

mb_detect_encoding

Detectar la codificación de caracteres

## Descripción

```php
mb_detect_encoding(string $string, [array $encodings], [bool $strict]): string
```php

Detectar la codificación de caracteres más probable para la `string` `string` desde una lista de candidatos.

A partir de PHP 8.1, esta función utiliza heurística para detectar cuál de las codificaciones de texto válidas en la lista especificada tiene más probabilidades de ser correcta y puede no estar en el orden de `encodings` proporcionado.

La detección automática del juego de caracteres previsto nunca es totalmente fiable; sin información adicional, es similar a descifrar una cadena cifrada sin la clave. Siempre es preferible utilizar una indicación del juego de caracteres almacenado o transmitido con los datos, como el encabezado HTTP "Content-Type".

Esta función se utiliza principalmente con codificaciones multibyte, donde no todas las secuencias de bytes forman una cadena válida. Si la cadena de entrada contiene una secuencia de este tipo, esta codificación será rechazada.

> [!WARNING]
> El nombre de esta función es engañoso, realiza una «suposición» en lugar de una «detección».
>
> Las suposiciones están lejos de ser precisas, y por lo tanto, esta función no permite detectar de manera fiable la codificación correcto de los caracteres.

## Parámetros

`string`  
El `string` que será inspeccionado.

`encodings`  
Una lista de codificaciones de caracteres a probar. Esta lista puede ser especificada como un `array` de `string`, o como un `string` único separado por comas.

Si `encodings` es omitido o `null`, el será utilizado el detect_order actual (definido con la opción de configuración [mbstring.detect_order](#ini.mbstring.detect-order), o la función `mb_detect_order`).

`strict`  
Controla el comportamiento cuando `string` no es válido en ninguno de los `encodings` listados. Si `strict` está definido como `false`, se devolverá la codificación más coincidente; si `strict` está definido como `true`, devolverá `false`.

El valor por omisión de `strict` puede ser definido con la opción de configuración [mbstring.strict_detection](#ini.mbstring.strict-detection).

## Valores devueltos

La codificación caracteres detectado, o `false` si la cadena no es válida en ninguna de las codificaciones listadas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | `mb_detect_encoding` ya no devolverá las siguientes codificaciones que no sean de texto: `"Base64"`, `"QPrint"`, `"UUencode"`, `"HTML entities"`, `"7 bit"` y `"8 bit"`. |

## Ejemplos

Ejemplo con `mb_detect_encoding`

```
<?php

$str = "\x95\xB6\x8E\x9A\x83\x52\x81\x5B\x83\x68";

// Detecta la codificación con el detect_order actual
var_dump(mb_detect_encoding($str));

// "auto" es modificado según mbstring.language
var_dump(mb_detect_encoding($str, "auto"));

// Especifica el parámetro "encodings" con una lista separada por comas
var_dump(mb_detect_encoding($str, "JIS, eucjp-win, sjis-win"));

// Uso de un array para especificar el parámetro "encodings"
$encodings = [
  "ASCII",
  "JIS",
  "EUC-JP"
];
var_dump(mb_detect_encoding($str, $encodings));
?>

    
```php

El ejemplo anterior mostrará:

    string(5) "ASCII"
    string(5) "ASCII"
    string(8) "SJIS-win"
    string(5) "ASCII"

Efecto del parámetro `strict`

```
<?php
// 'áéóú' codificado en ISO-8859-1
$str = "\xE1\xE9\xF3\xFA";

// La cadena no válica en ASCII ni UTF-8, pero UTF-8 se considera una coincidencia más cercana
var_dump(mb_detect_encoding($str, ['ASCII', 'UTF-8'], false));
var_dump(mb_detect_encoding($str, ['ASCII', 'UTF-8'], true));

// Si se encuentra una codificación válida, el parámetro "strict" no cambia el resultado
var_dump(mb_detect_encoding($str, ['ASCII', 'UTF-8', 'ISO-8859-1'], false));
var_dump(mb_detect_encoding($str, ['ASCII', 'UTF-8', 'ISO-8859-1'], true));
?>

    
```php

El ejemplo anterior mostrará:

    string(5) "UTF-8"
    bool(false)
    string(10) "ISO-8859-1"
    string(10) "ISO-8859-1"

En ciertos casos, la misma secuencia de bytes puede formar una cadena válida en diferentes codificaciones de caracteres, y es imposible determinar cuál interpretación era prevista. Un ejemplo, entre otros, la secuencia de bytes "\xC4\xA2" podría ser:

"Ä¢" (U+00C4 LATIN CAPITAL LETTER A WITH DIAERESIS seguido de U+00A2 CENT SIGN) codificado en ISO-8859-1, ISO-8859-15, o Windows-1252, "ФЂ" (U+0424 CYRILLIC CAPITAL LETTER EF seguido de U+0402 CYRILLIC CAPITAL LETTER DJE) codificado en ISO-8859-5, "Ģ" (U+0122 LATIN CAPITAL LETTER G WITH CEDILLA) codificado en UTF-8

Efecto del orden cuando coinciden múltiples codificaciones

```
<?php
$str = "\xC4\xA2";

// La cadena es válida en las tres codificaciones, pero no siempre devolverá el primero de la lista
var_dump(mb_detect_encoding($str, ['UTF-8']));
var_dump(mb_detect_encoding($str, ['UTF-8', 'ISO-8859-1', 'ISO-8859-5'])); // A partir de PHP 8.1 esto devolverá ISO-8859-1 en vez de UTF-8
var_dump(mb_detect_encoding($str, ['ISO-8859-1', 'ISO-8859-5', 'UTF-8']));
var_dump(mb_detect_encoding($str, ['ISO-8859-5', 'UTF-8', 'ISO-8859-1']));
?>

    
```php

El ejemplo anterior mostrará:

    string(5) "UTF-8"
    string(10) "ISO-8859-1"
    string(10) "ISO-8859-1"
    string(10) "ISO-8859-5"

## Véase también

`mb_detect_order`
