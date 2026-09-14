---
title: metaphone
description: Calcula la clave metaphone
source_url: https://www.php.net/manual/es/function.metaphone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/metaphone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 873f4a3d5
order: 88900
---

metaphone

Calcula la clave metaphone

## Descripción

```php
metaphone(string $string, [int $max_phonemes]): string
```php

Calcula la clave metaphone de `string`.

`metaphone` es similar a la función `soundex`: crea una clave similar para palabras cuya pronunciación es cercana. Es una función más precisa que `soundex` ya que tiene en cuenta la pronunciación inglesa. La clave metaphone generada es de tamaño variable.

Metaphone fue desarrollado por Lawrence Philips \<lphilips at verity dot com\>. Este método está descrito en el libro `["Practical Algorithms for Programmers", Binstock & Rex, Addison Wesley, 1995]`.

## Parámetros

`string`  
La cadena de entrada.

`max_phonemes`  
Este parámetro restringe la clave metaphone devuelta a una longitud de `max_phonemes` *caracteres*. Sin embargo, los fonemas resultantes siempre se transcriben completamente, por lo que la longitud de la cadena resultante puede ser ligeramente más larga que `max_phonemes`. El valor por omisión es `0`, lo que significa que no se aplicará ninguna limitación.

## Valores devueltos

Devuelve la clave metaphone, en forma de `string`.

## Historial de cambios

| Versión | Descripción                                     |
|---------|-------------------------------------------------|
| 8.0.0   | Esta función devolvía `false` en caso de error. |

## Ejemplos

Ejemplo con `metaphone`

```
<?php
var_dump(metaphone('programming'));
var_dump(metaphone('programmer'));
?>

    
```php

El ejemplo anterior mostrará:

    string(7) "PRKRMNK"
    string(6) "PRKRMR"

Utilización del parámetro `max_phonemes`

```
<?php
var_dump(metaphone('programming', 5));
var_dump(metaphone('programmer', 5));
?>

    
```php

El ejemplo anterior mostrará:

    string(5) "PRKRM"
    string(5) "PRKRM"

Utilizando el parámetro `max_phonemes`

En este ejemplo, `metaphone` está configurado para producir una cadena de cinco caracteres, pero esto requeriría dividir el fonema final (`'x'` se supone que se transcribe como `'KS'`), por lo que la función devuelve una cadena de seis caracteres.

```
     
<?php
var_dump(metaphone('Asterix', 5));
?>

    
```php

El ejemplo anterior mostrará:

         
    string(6) "ASTRKS"

## Véase también

`levenshtein`, `similar_text`, `soundex`
