---
title: utf8_encode
description: Convierte una cadena ISO-8859-1 a UTF-8
source_url: https://www.php.net/manual/es/function.utf8-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/utf8-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 89590
---

utf8_encode

Convierte una cadena ISO-8859-1 a UTF-8

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] utf8_encode(string $string): string
```php

Esta función convierte la cadena `string` desde la codificación `ISO-8859-1` a `UTF-8`.

> [!NOTE]
> Esta función no intenta adivinar la codificación actual de la cadena de caracteres proporcionada, asume que está codificada en ISO-8859-1 (también conocido como "Latin 1") y la convierte a UTF-8. Dado que cada secuencia de bytes es una cadena de caracteres ISO-8859-1 válida, nunca habrá errores, pero no resultará en una cadena de caracteres útil si se esperaba una codificación diferente.
>
> Muchas páginas web marcadas como que utilizan la codificación de caracteres `ISO-8859-1` utilizan efectivamente una codificación similar a `Windows-1252`, y los navegadores web interpretarán las páginas web `ISO-8859-1` como `Windows-1252`. Las características adicionales de `Windows-1252` son caracteres imprimibles, tales como el signo euro (`€`) y las comillas curvas (`“` `”`), en lugar de algunos caracteres de control de `ISO-8859-1`. Esta función no convertirá estos caracteres `Windows-1252` correctamente. Utilice una función diferente si se necesita una conversión `Windows-1252`.

## Parámetros

`string`  
Una cadena ISO-8859-1.

## Valores devueltos

Devuelve la versión UTF-8 de `string`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ha sido declarada obsoleta. |
| 7.2.0 | Esta función fue movida al núcleo de PHP, anteriormente, era necesario instalar la extensión XML para utilizarla. |

## Ejemplos

Ejemplo de uso

```
<?php
// Convierte la cadena 'Zoë' de ISO 8859-1 a UTF-8
$iso8859_1_string = "\x5A\x6F\xEB";
$utf8_string = utf8_encode($iso8859_1_string);
echo bin2hex($utf8_string), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    5a6fc3ab

## Notas

> [!NOTE]
> Esta función está *obsoleta* a partir de PHP 8.2.0 y será eliminada en una versión futura. Los usos existentes deberían ser verificados y reemplazados por alternativas apropiadas.
>
> Una funcionalidad similar puede ser obtenida con `mb_convert_encoding`, que soporta ISO-8859-1 y muchos otros juegos de caracteres.
>
> <div class="informalexample">
>
> ```
> <?php
> $iso8859_1_string = "\xEB"; // 'ë' (e con diéresis) en ISO-8859-1
> $utf8_string = mb_convert_encoding($iso8859_1_string, 'UTF-8', 'ISO-8859-1');
> echo bin2hex($utf8_string), "\n";
>
> $iso8859_7_string = "\xEB"; // la misma cadena en ISO-8859-7 representa 'λ' (lambda minúscula griega)
> $utf8_string = mb_convert_encoding($iso8859_7_string, 'UTF-8', 'ISO-8859-7');
> echo bin2hex($utf8_string), "\n";
>
> $windows_1252_string = "\x80"; // '€' (signo euro) en Windows-1252, pero no en ISO-8859-1
> $utf8_string = mb_convert_encoding($windows_1252_string, 'UTF-8', 'Windows-1252');
> echo bin2hex($utf8_string), "\n";
> ?>
>           
>         
> ```
>
> El ejemplo anterior mostrará:
>
>     c3ab
>     cebb
>     e282ac
>
>             
>
> </div>
>
> Otras opciones pueden estar disponibles dependiendo de las extensiones instaladas, tales como UConverter::transcode y `iconv`.
>
> Los siguientes ejemplos dan todos el mismo resultado:
>
> <div class="informalexample">
>
> ```
> <?php
> $iso8859_1_string = "\x5A\x6F\xEB"; // 'Zoë' en ISO-8859-1
>
> $utf8_string = utf8_encode($iso8859_1_string);
> echo bin2hex($utf8_string), "\n";
>
> $utf8_string = mb_convert_encoding($iso8859_1_string, 'UTF-8', 'ISO-8859-1');
> echo bin2hex($utf8_string), "\n";
>
> $utf8_string = UConverter::transcode($iso8859_1_string, 'UTF8', 'ISO-8859-1');
> echo bin2hex($utf8_string), "\n";
>
> $utf8_string = iconv('ISO-8859-1', 'UTF-8', $iso8859_1_string);
> echo bin2hex($utf8_string), "\n";
> ?>
>           
>         
> ```
>
> El ejemplo anterior mostrará:
>
>     5a6fc3ab
>     5a6fc3ab
>     5a6fc3ab
>     5a6fc3ab
>
>             
>
> </div>

## Véase también

`utf8_decode`, `mb_convert_encoding`, UConverter::transcode, `iconv`
