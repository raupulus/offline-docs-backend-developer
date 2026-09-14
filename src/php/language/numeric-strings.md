---
title: Strings numéricos
source_url: https://www.php.net/manual/es/language.types.numeric-strings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/numeric-strings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: e587d0655
order: 4490
---

## Strings numéricos

Un `string` PHP se considera numérico si puede ser interpretado como un `int` o un `float`.

Formalmente a partir de PHP 8.0.0:

    WHITESPACES      \s*
    LNUM             [0-9]+
    DNUM             ([0-9]*[\.]{LNUM}) | ({LNUM}[\.][0-9]*)
    EXPONENT_DNUM    (({LNUM} | {DNUM}) [eE][+-]? {LNUM})
    INT_NUM_STRING   {WHITESPACES} [+-]? {LNUM} {WHITESPACES}
    FLOAT_NUM_STRING {WHITESPACES} [+-]? ({DNUM} | {EXPONENT_DNUM}) {WHITESPACES}
    NUM_STRING       ({INT_NUM_STRING} | {FLOAT_NUM_STRING})

PHP también dispone de un concepto de strings *iniciando* numéricamente. Se trata simplemente de un string que comienza como un string numérico seguido de cualquier carácter.

> [!NOTE]
> Cualquier string que contenga la letra `E` (insensible a mayúsculas y minúsculas) delimitada por números será considerada como un número expresado en notación científica. Esto puede producir resultados inesperados.
>
> <div class="example">
>
> <div class="title">
>
> Scientific Notation Comparisons
>
> </div>
>
> ```
> <?php
> var_dump("0D1" == "000"); // false, "0D1" no es notación científica
> var_dump("0E1" == "000"); // true, "0E1" es 0 * (10 ^ 1), o 0
> var_dump("2E1" == "020"); // true, "2E1" es 2 * (10 ^ 1), o 20
> ?>
>
>    
> ```
>
> </div>

## Strings utilizados en contextos numéricos

Cuando una `string` debe ser evaluada como un número (por ejemplo, operaciones aritméticas, declaración de tipo `int`, etc.), se siguen los siguientes pasos para determinar el resultado:

1.  Si el `string` es numérico, se resuelve en `int` si el `string` es un string numérico entero y entra dentro de los límites del tipo `int` (tales como definidas por `PHP_INT_MAX`), de lo contrario se resuelve en un `float`.

2.  Si el contexto permite los strings iniciando numéricamente y el `string` es uno de ellos, se resuelve en `int` si la parte inicial del `string` es un string numérico entero y entra dentro de los límites del tipo `int` (tales como definidas por `PHP_INT_MAX`), de lo contrario se resuelve en un `float`. Además, se genera un error de nivel `E_WARNING`.

3.  Si la `string` no es numérica, se lanza una `TypeError`.

## Comportamiento anterior a PHP 8.0.0

Antes de PHP 8.0.0, un `string` se consideraba numérico solo si tenía espacios en blanco al *inicio* del string, si tenía espacios en blanco al *final* del string, el string se consideraba como un string iniciando numéricamente.

Antes de PHP 8.0.0, cuando un string se utilizaba en un contexto numérico, seguía los mismos pasos que los anteriores, con las siguientes diferencias:

- El uso de un string iniciando numéricamente generaba un error de tipo `E_NOTICE` en lugar de `E_WARNING`.

- Si el string no era numérico, se generaba un `E_WARNING` y se devolvía el valor `0`.

Anterior a PHP 7.1.0, ni `E_NOTICE` ni `E_WARNING` se generaban.

```php
<?php
$foo = 1 + "10.5";                // $foo es float (11.5)
$foo = 1 + "-1.3e3";              // $foo es float (-1299)
$foo = 1 + "bob-1.3e3";           // TypeError a partir de PHP 8.0.0, $foo era integer (1) anteriormente
$foo = 1 + "bob3";                // TypeError a partir de PHP 8.0.0, $foo era integer (1) anteriormente
$foo = 1 + "10 Small Pigs";       // $foo es integer (11) y se genera un E_WARNING en PHP 8.0.0, E_NOTICE anteriormente
$foo = 4 + "10.2 Little Piggies"; // $foo es float (14.2) y se genera un E_WARNING en PHP 8.0.0, E_NOTICE anteriormente
$foo = "10.0 pigs " + 1;          // $foo es float (11) y se genera un E_WARNING en PHP 8.0.0, E_NOTICE anteriormente
$foo = "10.0 pigs " + 1.0;        // $foo es float (11) y se genera un E_WARNING en PHP 8.0.0, E_NOTICE anteriormente
?>

   
```
