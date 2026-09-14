---
title: crc32
description: Calcula la suma de comprobación CRC32
source_url: https://www.php.net/manual/es/function.crc32.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/crc32.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 88690
---

crc32

Calcula la suma de comprobación CRC32

## Descripción

```php
crc32(string $string): int
```php

Genera la suma de comprobación cíclica CRC32, calculada en 32 bits, y aplicada a la cadena `string`. Esta función se utiliza generalmente para validar la integridad de los datos durante una transmisión.

> [!WARNING]
> Debido a que el tipo entero de PHP es firmado, la mayoría de las sumas de comprobación crc32 resultan ser enteros negativos en plataformas de 32 bits. En instalaciones de 64 bits, todos los resultados de la función `crc32` serán enteros positivos.
>
> Asimismo, se debe utilizar el formateador "%u" de la función `sprintf` o de la función `printf` para obtener una representación en cadena de caracteres de la suma de comprobación no firmada de la función `crc32` en formato decimal.
>
> Para una representación hexadecimal de la suma de comprobación, se puede utilizar el formateador "%x" de la función `sprintf` o de la función `printf`, o bien las funciones de conversión `dechex`, ambas soluciones se encargan de convertir el resultado de la función `crc32` en un entero no firmado.
>
> En instalaciones de 64 bits, la función también devolverá enteros negativos para valores devueltos muy grandes, pero esto romperá la conversión hexadecimal al tener una posición adicional 0xFFFFFFFF########. Sabiendo que la representación decimal parece ser el caso más ampliamente utilizado, se ha decidido no romperla incluso si esto rompe directamente la comparación decimal en el 50% de los casos al pasar de 32 a 64 bits.
>
> Con perspectiva, el hecho de que la función devuelva un entero quizá no fue la mejor idea, y devolver desde el principio una representación hexadecimal en forma de cadena de caracteres (tal como hace la función `md5`), habría sido una mejor solución.
>
> Para una solución más duradera, se puede recurrir a la función genérica `hash`. `hash("crc32b", $str)` devolverá la misma cadena de caracteres que `str_pad(dechex(crc32($str)), 8, '0', STR_PAD_LEFT)`.

## Parámetros

`string`  
Los datos.

## Valores devueltos

Devuelve la suma de comprobación crc32 de la cadena `string`, en forma de un entero.

## Ejemplos

Mostrar una suma de comprobación CRC32

Este ejemplo ilustra cómo mostrar la suma de comprobación con la función `printf`:

```
<?php
$checksum = crc32("Le vif zéphyr jubile sur les kumquats du clown gracieux.");
printf("%u\n", $checksum);
?>

    
```php

## Véase también

`hash`, `md5`, `sha1`
