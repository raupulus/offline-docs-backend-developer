---
title: substr_count
description: Cuenta el número de ocurrencias de segmentos en un string
source_url: https://www.php.net/manual/es/function.substr-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/substr-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89520
---

substr_count

Cuenta el número de ocurrencias de segmentos en un string

## Descripción

```php
substr_count(string $haystack, string $needle, [int $offset], [int $length]): int
```php

`substr_count` devuelve el número de ocurrencias de `needle` en el string `haystack`. Tenga en cuenta que `needle` es sensible a mayúsculas y minúsculas.

> [!NOTE]
> Esta función no cuenta los strings que se solapan. Véase el ejemplo a continuación.

## Parámetros

`haystack`  
El string en el que se busca

`needle`  
El string que se busca

`offset`  
El desplazamiento desde donde se comienza a contar. Si la posición es negativa, el conteo comienza desde el final del string.

`length`  
La longitud máxima después del desplazamiento especificado para buscar el string. La función emite un error si el desplazamiento más la longitud es mayor que la longitud de `haystack`. Una longitud negativa hará que el conteo comience al final de `haystack`.

## Valores devueltos

Esta función devuelve un `int`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `length` ahora puede ser nullable. |
| 7.1.0 | Se agregó soporte para números negativos para `offset` y `length`. `length` también puede ser `0` ahora. |

## Ejemplos

Ejemplo con `substr_count`

```
<?php
$text = 'Esto es una prueba';
echo strlen($text), PHP_EOL; // 16

echo substr_count($text, 'es'), PHP_EOL; // 2

// el string se reduce a 'st una prueba', por lo que muestra 1
echo substr_count($text, 'es', 6), PHP_EOL;

// el texto se reduce a 'st u', por lo que muestra 0
echo substr_count($text, 'is', 3, 3), PHP_EOL;

// muestra solo 1, porque no cuenta los strings
// que se solapan
$text2 = 'gcdgcdgcd';
echo substr_count($text2, 'gcdgcd'), PHP_EOL;

// lanza una excepción porque 5+10 > 14
echo substr_count($text, 'is', 5, 10), PHP_EOL;
?>

    
```php

## Véase también

`count_chars`, `strpos`, `substr`, `strstr`
