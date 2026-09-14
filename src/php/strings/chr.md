---
title: chr
description: Generar un string de un byte a partir de un número
source_url: https://www.php.net/manual/es/function.chr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/chr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 88630
---

chr

Generar un string de un byte a partir de un número

## Descripción

```php
chr(int $codepoint): string
```php

Devuelve un `string` de un solo carácter que contiene el carácter especificado al interpretar `codepoint` como un `int` sin signo.

Esto puede ser utilizado para crear un `string` de un solo carácter en una codificación de un byte como ASCII, ISO-8859 o Windows 1252, pasando la posición del carácter deseado en la tabla de correspondencia de la codificación. Sin embargo, es importante tener en cuenta que esta función no es consciente de ninguna codificación de `string`, y en particular no puede ser transmitido un valor de punto de código Unicode para generar un `string` en una codificación multibyte como UTF-8 o UTF-16.

Esta función complementa `ord`.

## Parámetros

`codepoint`  
Un `int` entre 0 y 255;

Los valores fuera del rango válido (0..255) serán convertidos a valor positivo, y terminarán en 255, lo que es equivalente al siguiente algoritmo:

```
while ($bytevalue < 0) {
    $bytevalue += 256;
}
$bytevalue %= 256;

       
```php

## Valores devueltos

Devuelve un `string` de un solo carácter que contiene el byte especificado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Pasar enteros fuera del intervalo `[0, 255]` ha quedado obsoleto. |
| 7.4.0 | Esta función ya no acepta silenciosamente los `codepoint`s no soportados, y convierte estos valores a `0`. |

## Ejemplos

Ejemplo con `chr`

```
<?php
// Supone que el string será utilizado como ASCII o una codificación
// compatible con este

$str = "The string ends in escape: ";

// Añade un carácter de escape al final del string $str
$str .= chr(27);
echo $str, PHP_EOL;
// Esto es a menudo más práctico, y realiza lo mismo

$str = sprintf("The string ends in escape: %c", 27);
echo $str, PHP_EOL;
?>

    
```php

Comportamiento de desbordamiento

```
<?php
echo chr(-159), chr(833), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    aA

Construir un string UTF-8 a partir de bytes individuales

```
<?php
$str = chr(240) . chr(159) . chr(144) . chr(152);
echo $str, PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    🐘

## Véase también

`sprintf` con el carácter de formato `%c`, `ord`, [Tabla ASCII](https://www.man7.org/linux/man-pages/man7/ascii.7.html), `mb_chr`, `IntlChar::chr`
