---
title: str_split
description: Convierte un string en un array
source_url: https://www.php.net/manual/es/function.str-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 31e301590
order: 89210
---

str_split

Convierte un string en un array

## Descripción

```php
str_split(string $string, [int $length]): array
```php

Convierte un string en un array.

## Parámetros

`string`  
El string de entrada.

`length`  
Longitud máxima de cada elemento.

## Valores devueltos

Si el argumento opcional `length` es especificado, el array devuelto será dividido en subpartes, cada una de tamaño `length`, a excepción de la última subparte que puede ser más corta si el string no se divide de manera equitativa. El valor por omisión de `length` es `1`, lo que significa que cada subparte tendrá un tamaño de un byte.

## Errores/Excepciones

Si `length` es menor que `1`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Si `string` está vacío, ahora se devuelve un array vacío. Anteriormente, se devolvía un array que contenía un único string vacío. |
| 8.0.0 | Si `length` es menor que `1`, se lanzará un `ValueError`; anteriormente, se emitía un error de tipo `E_WARNING` y la función devolvía `false`. |

## Ejemplos

Ejemplo con `str_split`

```
<?php

$str = "Hello Friend";

$arr1 = str_split($str);
$arr2 = str_split($str, 3);

print_r($arr1);
print_r($arr2);

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => H
        [1] => e
        [2] => l
        [3] => l
        [4] => o
        [5] =>
        [6] => F
        [7] => r
        [8] => i
        [9] => e
        [10] => n
        [11] => d
    )

    Array
    (
        [0] => Hel
        [1] => lo
        [2] => Fri
        [3] => end
    )

## Notas

> [!NOTE]
> `str_split` realizará la división a nivel de bits, en lugar de a nivel de caracteres al utilizarse con un string codificado en multibytes. `mb_str_split` puede ser utilizado para dividir el string en puntos de código. `grapheme_str_split` puede ser utilizado para dividir el string en clusters de grafemas.

## Véase también

`mb_str_split`, `grapheme_str_split`, `chunk_split`, `preg_split`, `explode`, `count_chars`, `str_word_count`, [for](#control-structures.for)
