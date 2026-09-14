---
title: str_pad
description: Completa un string hasta un tamaño dado
source_url: https://www.php.net/manual/es/function.str-pad.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-pad.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 89160
---

str_pad

Completa un string hasta un tamaño dado

## Descripción

```php
str_pad(string $string, int $length, [string $pad_string], [int $pad_type]): string
```php

Retorna el string `string`, completado a la derecha, a la izquierda o en ambos lados, con el string `pad_string` hasta que alcance el tamaño de `length`.

## Parámetros

`string`  
El string de entrada.

`length`  
La longitud deseada del string final completado. Si el valor de `length` es negativo, menor que, o igual al tamaño actual del string `string`, `string` se retorna sin cambios.

`pad_string`  
> [!NOTE]
> El argumento `pad_string` puede ser truncado si el número de caracteres de completado no es múltiplo del tamaño de `pad_string`.

`pad_type`  
El argumento opcional `pad_type` puede ser una de las constantes siguientes: `STR_PAD_RIGHT`, `STR_PAD_LEFT`, o `STR_PAD_BOTH`. Si `pad_type` no es especificado, toma el valor por omisión de `STR_PAD_RIGHT`.

## Valores devueltos

Retorna el string completado.

## Ejemplos

Ejemplo con `str_pad`

```
<?php
$input = "Alien";
echo str_pad($input, 10), PHP_EOL;                      // produce "Alien     "
echo str_pad($input, 10, "-=", STR_PAD_LEFT), PHP_EOL;  // produce "-=-=-Alien"
echo str_pad($input, 10, "_", STR_PAD_BOTH), PHP_EOL;   // produce "__Alien___"
echo str_pad($input,  6, "___"), PHP_EOL;               // produce "Alien_"
echo str_pad($input,  3, "*"), PHP_EOL;                 // produce "Alien"
?>

    
```php

## Véase también

`mb_str_pad`
