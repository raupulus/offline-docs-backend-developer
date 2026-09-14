---
title: UConverter::transcode
description: Convierte una cadena de un juego de caracteres a otro
source_url: https://www.php.net/manual/es/uconverter.transcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/uconverter/transcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42800
---

UConverter::transcode

Convierte una cadena de un juego de caracteres a otro

## Descripción

```php
public static UConverter::transcode(string $str, string $toEncoding, string $fromEncoding, [array $options]): string
```php

Convierte `str` de `fromEncoding` a `toEncoding`.

## Parámetros

`str`  
El `string` a convertir.

`toEncoding`  
El juego de caracteres deseado para el resultado.

`fromEncoding`  
El juego de caracteres actual utilizado para interpretar `str`.

`options`  
Un `array` opcional, que puede contener las siguientes claves: `'to_subst'` - el carácter de sustitución a utilizar en lugar de cualquier carácter de `str` que no pueda ser codificado en `toEncoding`. Si se especifica, debe representar un solo carácter en el codificación objetivo.

## Valores devueltos

Devuelve la cadena convertida, o `false` si ocurre un error.

## Ejemplos

Conversión de UTF-8 a UTF-16 y viceversa

```
<?php
$utf8_string = "\x5A\x6F\xC3\xAB"; // 'Zoë' en UTF-8
$utf16_string = UConverter::transcode($utf8_string, 'UTF-16BE', 'UTF-8');
echo bin2hex($utf16_string), "\n";

$new_utf8_string = UConverter::transcode($utf16_string, 'UTF-8', 'UTF-16BE');
echo bin2hex($new_utf8_string), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    005a006f00eb
    5a6fc3ab

Caracteres no válidos en la entrada

Si la cadena de entrada contiene una secuencia de octetos que no es válida en el codificación especificado por `fromEncoding`, son reemplazados por el punto de código Unicode U+FFFD (Carácter de reemplazo) antes de ser convertidos a `toEncoding`.

```
<?php
$invalid_utf8_string = "\xC3"; // secuencia multi-octetos UTF-8 incompleta
$utf16_string = UConverter::transcode($invalid_utf8_string, 'UTF-16BE', 'UTF-8');
echo bin2hex($utf16_string), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    fffd

Caracteres que no pueden ser codificados

Si la cadena de entrada contiene caracteres que no pueden ser representados en `toEncoding`, son reemplazados por un solo carácter. El carácter por defecto a utilizar depende del codificación y puede ser controlado mediante la opción `'to_subst'`.

```
<?php
$utf8_string = "\xE2\x82\xAC"; // € (símbolo euro) no existe en el ISO 8859-1

// El reemplazo por defecto en ISO 8859-1 es "\x1A" (Sustituto)
$iso8859_1_string = UConverter::transcode($utf8_string, 'ISO-8859-1', 'UTF-8');
echo bin2hex($iso8859_1_string), "\n";

// Especifica un reemplazo de '?' ("\x3F") en su lugar
$iso8859_1_string = UConverter::transcode(
    $utf8_string, 'ISO-8859-1', 'UTF-8', ['to_subst' => '?']
);
echo bin2hex($iso8859_1_string), "\n";

// Dado que el ISO 8859-1 no puede mapear U+FFFD, la entrada inválida también es reemplazada por to_subst.
$invalid_utf8_string = "\xC3"; // secuencia multi-octetos UTF-8 incompleta
$iso8859_1_string = UConverter::transcode(
    $invalid_utf8_string, 'ISO-8859-1', 'UTF-8', ['to_subst' => '?']
);
echo bin2hex($iso8859_1_string), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    1a
    3f
    3f

## Véase también

`mb_convert_encoding`, `iconv`
