---
title: soundex
description: Calcula la clave soundex
source_url: https://www.php.net/manual/es/function.soundex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/soundex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 873f4a3d5
order: 89070
---

soundex

Calcula la clave soundex

## Descripción

```php
soundex(string $string): string
```php

Calcula la clave soundex de la cadena `string`.

La clave soundex posee la propiedad de que dos palabras pronunciadas de manera similar tendrán la misma clave soundex. Esta función se utiliza, por lo tanto, para simplificar las búsquedas en las bases de datos, donde se conoce la pronunciación de una palabra o nombre, pero no su ortografía exacta.

La implementación de la función soundex de PHP ha sido descrita por Donald Knuth en `"The Art Of Computer Programming, vol. 3: Sorting And Searching", Addison-Wesley (1973), pp. 391-392`.

## Parámetros

`string`  
La cadena de entrada.

## Valores devueltos

Retorna la clave soundex como `string` con cuatro caracteres. Si al menos una letra está contenida en `string`, la cadena retornada comienza con una letra. De lo contrario, se retorna `"0000"`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Antes de esta versión, llamar a la función con una cadena vacía retornaba `false` sin ninguna razón en particular. |

## Ejemplos

Ejemplos de Soundex

```
<?php
echo soundex("Euler"), PHP_EOL, soundex("Ellery"), PHP_EOL;

soundex("Euler")       == soundex("Ellery");    // E460
soundex("Gauss")       == soundex("Ghosh");     // G200
soundex("Hilbert")     == soundex("Heilbronn"); // H416
soundex("Knuth")       == soundex("Kant");      // K530
soundex("Lloyd")       == soundex("Ladd");      // L300
soundex("Lukasiewicz") == soundex("Lissajous"); // L222
?>

    
```php

## Véase también

`levenshtein`, `metaphone`, `similar_text`
