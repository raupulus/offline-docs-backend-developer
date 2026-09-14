---
title: utf8_decode
description: Convierte una string UTF-8 a ISO-8859-1, reemplazando los caracteres
  no válidos o no representables.
source_url: https://www.php.net/manual/es/function.utf8-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/utf8-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 330a38c4d
order: 89580
---

utf8_decode

Convierte una string UTF-8 a ISO-8859-1, reemplazando los caracteres no válidos o no representables.

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] utf8_decode(string $string): string
```php

`utf8_decode` decodifica la string `string`, asumiendo que está en formato `UTF-8`, y la convierte al formato `ISO-8859-1`. Los bytes en la string que no son válidos en `UTF-8` y los caracteres `UTF-8` que no existen en `ISO-8859-1` (que son, los caracteres por encima de `U+00FF`) son reemplazados por `?`.

> [!NOTE]
> Numerosas páginas web marcadas como utilizando la codificación de caracteres `ISO-8859-1` utilizan efectivamente una codificación similar a `Windows-1252`, y los navegadores web interpretarán las páginas web `ISO-8859-1` como `Windows-1252`. Las características adicionales de `Windows-1252` son caracteres imprimibles, tales como el signo euro (`€`) y las comillas curvas (`“` `”`), en lugar de ciertos caracteres de control de `ISO-8859-1`. Esta función no convertirá correctamente estos caracteres `Windows-1252`. Utilice una función diferente si se requiere una conversión `Windows-1252`.

## Parámetros

`string`  
La string codificada en UTF-8.

## Valores devueltos

Devuelve la string `string` convertida a ISO-8859-1.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ha sido declarada obsoleta. |
| 7.2.0 | Esta función fue movida al núcleo de PHP; anteriormente, era necesario instalar la extensión XML para utilizarla. |

## Ejemplos

Ejemplo de uso

```
<?php
// Convierte la string 'Zoë' de UTF-8 a ISO 8859-1
$utf8_string = "\x5A\x6F\xC3\xAB";
$iso8859_1_string = utf8_decode($utf8_string);
echo bin2hex($iso8859_1_string), "\n";

// Las secuencias UTF-8 no válidas son reemplazadas por '?'
$invalid_utf8_string = "\xC3";
$iso8859_1_string = utf8_decode($invalid_utf8_string);
var_dump($iso8859_1_string);

// Los caracteres que no existen en la norma ISO 8859-1,
// tales como '€' (signo del euro) son igualmente reemplazados por '?'
$utf8_string = "\xE2\x82\xAC";
$iso8859_1_string = utf8_decode($utf8_string);
var_dump($iso8859_1_string);
?>

   
```php

El ejemplo anterior mostrará:

    5a6feb
    string(1) "?"
    string(1) "?"

## Notas

> [!NOTE]
> Esta función está *obsoleta* a partir de PHP 8.2.0 y será eliminada en una versión futura. Los usos existentes deberían ser verificados y reemplazados por alternativas apropiadas.
>
> Una funcionalidad similar puede obtenerse con `mb_convert_encoding`, que soporta ISO-8859-1 y numerosos otros juegos de caracteres.
>
> <div class="informalexample">
>
> ```
> <?php
> $utf8_string = "\xC3\xAB"; // 'ë' (e con diéresis) en UTF-8
> $iso8859_1_string = mb_convert_encoding($utf8_string, 'ISO-8859-1', 'UTF-8');
> echo bin2hex($iso8859_1_string), "\n";
>
> $utf8_string = "\xCE\xBB"; // 'λ' (lambda minúscula griega) en UTF-8
> $iso8859_7_string = mb_convert_encoding($utf8_string, 'ISO-8859-7', 'UTF-8');
> echo bin2hex($iso8859_7_string), "\n";
>
> $utf8_string = "\xE2\x82\xAC"; // '€' (signo del euro) en UTF-8 (no presente en ISO-8859-1)
> $windows_1252_string = mb_convert_encoding($utf8_string, 'Windows-1252', 'UTF-8');
> echo bin2hex($windows_1252_string), "\n";
> ?>
>           
>         
> ```
>
> El ejemplo anterior mostrará:
>
>     eb
>     eb
>     80
>
>             
>
> </div>
>
> Otras opciones pueden estar disponibles dependiendo de las extensiones instaladas, tales como UConverter::transcode y `iconv`.
>
> Los siguientes ejemplos producen todos el mismo resultado:
>
> <div class="informalexample">
>
> ```
> <?php
> $utf8_string = "\x5A\x6F\xC3\xAB"; // 'Zoë' en UTF-8
> $iso8859_1_string = utf8_decode($utf8_string);
> echo bin2hex($iso8859_1_string), "\n";
>
> $iso8859_1_string = mb_convert_encoding($utf8_string, 'ISO-8859-1', 'UTF-8');
> echo bin2hex($iso8859_1_string), "\n";
>
> $iso8859_1_string = iconv('UTF-8', 'ISO-8859-1', $utf8_string);
> echo bin2hex($iso8859_1_string), "\n";
>
> $iso8859_1_string = UConverter::transcode($utf8_string, 'ISO-8859-1', 'UTF8');
> echo bin2hex($iso8859_1_string), "\n";
> ?>
>           
>         
> ```
>
> El ejemplo anterior mostrará:
>
>     5a6feb
>     5a6feb
>     5a6feb
>     5a6feb
>
>             
>
> </div>
>
> Al especificar `'?'` como opción `'to_subst'` para UConverter::transcode, se obtiene el mismo resultado que `utf8_decode` para las strings que son inválidas o que no pueden ser representadas en ISO 8859-1.
>
> <div class="informalexample">
>
> ```
> <?php
> $utf8_string = "\xE2\x82\xAC"; // € (signo del euro) no existe en ISO 8859-1
> $iso8859_1_string = UConverter::transcode(
>     $utf8_string, 'ISO-8859-1', 'UTF-8', ['to_subst' => '?']
> );
> var_dump($iso8859_1_string);
> ?>
>           
>         
> ```
>
> El ejemplo anterior mostrará:
>
>     string(1) "?"
>
>             
>
> </div>

## Véase también

`utf8_encode`, `mb_convert_encoding`, UConverter::transcode, `iconv`
