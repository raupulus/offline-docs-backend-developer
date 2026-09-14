---
title: ord
description: Convierte el primer byte de un string en un valor entre 0 y 255
source_url: https://www.php.net/manual/es/function.ord.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/ord.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 88950
---

ord

Convierte el primer byte de un string en un valor entre 0 y 255

## Descripción

```php
ord(string $character): int
```php

Interpreta el valor binario del primer byte de `character` como un `int` sin signo entre 0 y 255.

Si el `string` está en una codificación de un byte como ASCII, ISO-8859 o Windows 1252, esto es equivalente a devolver la posición de un carácter en la tabla de correspondencia de la codificación. Sin embargo, cabe señalar que esta función no es consciente de ninguna codificación de `string`, y en particular nunca identificará un valor de punto de código Unicode en una codificación multibyte como UTF-8 o UTF-16.

Esta función complementa `chr`.

## Parámetros

`character`  
Un carácter.

## Valores devueltos

Un `int` entre 0 y 255.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.5.0   | Pasar un string que no sea un único byte ha quedado obsoleto. |

## Ejemplos

Ejemplo con `ord`

```
<?php
$str = "\n";
if (ord($str) == 10) {
  echo "El primer carácter de \$str es un salto de línea\n";
}
?>

    
```php

Examinar los bytes individuales de un string UTF-8

```
<?php
$str = "🐘";
for ( $pos=0; $pos < strlen($str); $pos ++ ) {
 $byte = substr($str, $pos);
 echo 'Byte ' . $pos . ' de $str tiene como valor ' . ord($byte) . PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    Byte 0 de $str tiene como valor 240
    Byte 1 de $str tiene como valor 159
    Byte 2 de $str tiene como valor 144
    Byte 3 de $str tiene como valor 152

## Véase también

`chr`, [Tabla ASCII](https://www.man7.org/linux/man-pages/man7/ascii.7.html), `mb_ord`, `IntlChar::ord`
