---
title: substr_compare
description: Comparar dos strings desde un offset hasta una longitud en caracteres
source_url: https://www.php.net/manual/es/function.substr-compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/substr-compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 89510
---

substr_compare

Comparar dos strings desde un offset hasta una longitud en caracteres

## Descripción

```php
substr_compare(string $haystack, string $needle, int $offset, [int $length], [bool $case_insensitive]): int
```php

`substr_compare` compara `haystack` desde la posición `offset` con `needle` durante `length` caracteres.

## Parámetros

`haystack`  
El string principal a comparar.

`needle`  
El string secundario a comparar.

`offset`  
La posición de inicio para la comparación. Si es un valor negativo, se comienza a contar desde el final del string.

`length`  
La longitud de la comparación. El valor por omisión es el máximo entre la longitud de `needle` y la longitud de `haystack` menos el parámetro `offset`.

`case_insensitive`  
Si `case_insensitive` vale `true`, la comparación no distingue entre mayúsculas y minúsculas.

## Valores devueltos

Devuelve un valor inferior a 0 si `string1` es inferior a `string2`; un valor superior a 0 si `string1` es superior a `string2`, y `0` si son iguales. No se puede deducir ningún significado particular de este valor, excepto su signo.

Si `length` es igual (anterior a PHP 7.2.18, 7.3.5) o mayor que el tamaño de `haystack` o que `length` está definido y es inferior a 0, `substr_compare` muestra una alerta y retorna `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ya no garantiza retornar `strlen($string1) - strlen($string2)` cuando las longitudes de las strings no son iguales, y puede retornar `-1` o `1` en su lugar. |
| 8.0.0 | `length` ahora es nullable. |
| 7.2.18, 7.3.5 | `offset` ahora puede ser igual al tamaño de `haystack`. |

## Ejemplos

Ejemplo con `substr_compare`

```
<?php
echo substr_compare("abcde", "bc", 1, 2), PHP_EOL; // 0
echo substr_compare("abcde", "de", -2, 2), PHP_EOL; // 0
echo substr_compare("abcde", "bcg", 1, 2), PHP_EOL; // 0
echo substr_compare("abcde", "BC", 1, 2, true), PHP_EOL; // 0
echo substr_compare("abcde", "bc", 1, 3), PHP_EOL; // 1
echo substr_compare("abcde", "cd", 1, 2), PHP_EOL; // -1
echo substr_compare("abcde", "abc", 5, 1), PHP_EOL; // -1
?>

    
```php

## Véase también

`strncmp`
