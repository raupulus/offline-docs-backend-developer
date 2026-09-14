---
title: localeconv
description: Lee la configuración local
source_url: https://www.php.net/manual/es/function.localeconv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/localeconv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 715a125af
order: 88860
---

localeconv

Lee la configuración local

## Descripción

```php
localeconv(): array
```php

Devuelve un array asociativo que contiene la información de formatos localizados para números y moneda.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`localeconv` devuelve los formatos según la configuración realizada con `setlocale`. El array asociativo que se devuelve contiene los siguientes índices:

| Índice del array | Descripción |
|----|----|
| `decimal_point` | Separador decimal |
| `thousands_sep` | Separador de miles |
| `grouping` | Array que contiene los agrupamientos numéricos |
| `int_curr_symbol` | Símbolo monetario internacional (p.ej. EUR) |
| `currency_symbol` | Símbolo monetario local (p.ej. ¤) |
| `mon_decimal_point` | Separador decimal monetario |
| `mon_thousands_sep` | Separador de miles monetario |
| `mon_grouping` | Array que contiene los agrupamientos numéricos monetarios |
| `positive_sign` | Signo para valores positivos |
| `negative_sign` | Signo para valores negativos |
| `int_frac_digits` | Número internacional de decimales |
| `frac_digits` | Número local de decimales |
| `p_cs_precedes` | `true` si `currency_symbol` precede a un valor positivo y `false` si le sigue. |
| `p_sep_by_space` | `true` si un espacio separa `currency_symbol` de un valor positivo, y `false` en caso contrario. |
| `n_cs_precedes` | `true` si `currency_symbol` precede a un valor negativo, y `false` si le sigue. |
| `n_sep_by_space` | `true` si un espacio separa `currency_symbol` de un valor negativo, y `false` en caso contrario. |
| `p_sign_posn` | 0 - Paréntesis rodean el valor y el símbolo monetario, 1 - El signo precede al valor y al símbolo monetario, 2 - El signo sigue al valor y al símbolo monetario, 3 - El signo precede inmediatamente al valor y al símbolo monetario, 4 - El signo sigue inmediatamente al valor y al símbolo monetario |
| `n_sign_posn` | 0 - Paréntesis rodean el valor y el símbolo monetario, 1 - El signo precede al valor y al símbolo monetario, 2 - El signo sigue al valor y al símbolo monetario, 3 - El signo precede inmediatamente al valor y al símbolo monetario, 4 - El signo sigue inmediatamente al valor y al símbolo monetario |

Los campos `p_sign_posn` y `n_sign_posn` contienen una cadena formateada de opciones. Cada número representa una de las condiciones listadas anteriormente.

Los campos de agrupamiento contienen arrays que definen cómo deben agruparse los números. Por ejemplo, el campo de agrupamiento monetario para `nl_NL` (en modo `UTF-8` con el símbolo euro), contendrá dos elementos, con los valores `3` y `3`. Si un elemento de array contiene `CHAR_MAX`, no se realiza ningún otro agrupamiento. Si un elemento de array contiene `0`, debe usarse el elemento anterior.

## Ejemplos

Ejemplo con `localeconv`

```
<?php
if (false !== setlocale(LC_ALL, 'nl_NL.UTF-8@euro')) {
    $locale_info = localeconv();
    print_r($locale_info);
}
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [decimal_point] => .
        [thousands_sep] =>
        [int_curr_symbol] => EUR
        [currency_symbol] => ¤
        [mon_decimal_point] => ,
        [mon_thousands_sep] =>
        [positive_sign] =>
        [negative_sign] => -
        [int_frac_digits] => 2
        [frac_digits] => 2
        [p_cs_precedes] => 1
        [p_sep_by_space] => 1
        [n_cs_precedes] => 1
        [n_sep_by_space] => 1
        [p_sign_posn] => 1
        [n_sign_posn] => 2
        [grouping] => Array
            (
            )

        [mon_grouping] => Array
            (
                [0] => 3
                [1] => 3
            )

    )

## Véase también

`setlocale`
