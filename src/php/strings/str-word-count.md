---
title: str_word_count
description: Cuenta el número de palabras utilizadas en un string
source_url: https://www.php.net/manual/es/function.str-word-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-word-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: d335ba69a
order: 89230
---

str_word_count

Cuenta el número de palabras utilizadas en un string

## Descripción

```php
str_word_count(string $string, [int $format], [string $characters]): array
```php

`str_word_count` cuenta el número de palabras en el string `string`. Si el argumento opcional `format` no está especificado, entonces el valor devuelto será un integer, representando el número de palabras encontradas. Si `format` está especificado, el valor devuelto será un array, que depende del formato `format`. Los valores posibles para `format` se listan a continuación.

En esta función, la noción de palabra depende de la configuración de la configuración local. Es un string que contiene todos los caracteres alfabéticos, y que puede contener, pero no comenzar por "'" y "-". Cabe señalar que las configuraciones locales multioctetos no están soportadas.

## Parámetros

`string`  
El string

`format`  
Especifica el valor de retorno de esta función. Los valores actualmente soportados son:

- 0: devuelve el número de palabras encontradas

- 1: devuelve un array que contiene todas las palabras encontradas dentro de `string`

- 2: devuelve un array asociativo, donde la clave indica la posición numérica de la palabra dentro de `string` y el valor es la palabra actual

`characters`  
Una lista de caracteres adicionales que serán considerados como una palabra

## Valores devueltos

Devuelve un array o un integer, dependiendo del `format` elegido.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `characters` ahora es nullable. |

## Ejemplos

Ejemplo con `str_word_count`

```
<?php

$str = "Salut l'ami, vous
        avez          une b3lle mine !";

print_r(str_word_count($str, 1));
print_r(str_word_count($str, 2));
print_r(str_word_count($str, 1, 'àáãç3'));

echo str_word_count($str);

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Salut
        [1] => l'ami
        [2] => vous
        [3] => avez
        [4] => une
        [5] => b
        [6] => lle
        [7] => mine
    )

    Array
    (
        [0] => Salut
        [6] => l'ami
        [13] => vous
        [27] => avez
        [41] => une
        [45] => b
        [47] => lle
        [51] => mine
    )

    Array
    (
        [0] => Salut
        [1] => l'ami
        [2] => vous
        [3] => avez
        [4] => une
        [5] => b3lle
        [6] => mine
    )

    8

## Véase también

`explode`, `preg_split`, `count_chars`, `substr_count`
