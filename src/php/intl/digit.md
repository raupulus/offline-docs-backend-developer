---
title: IntlChar::digit
description: Devuelve el dígito decimal de un punto de código para una base de numeración
  dada
source_url: https://www.php.net/manual/es/intlchar.digit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/digit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: fe67f9ad4
order: 40760
---

IntlChar::digit

Devuelve el dígito decimal de un punto de código para una base de numeración dada

## Descripción

```php
public static IntlChar::digit(int $codepoint, [int $base]): int
```php

Devuelve el valor decimal del punto de código en la base de numeración especificada.

Si la base de numeración no está en el rango `2 <= radix <= 36` o si el valor de `codepoint` no es un dígito válido en la base especificada, `false` es devuelto. Un carácter es un dígito válido si al menos una de las condiciones siguientes es verdadera: El carácter tiene un valor de dígito decimal. Estos caracteres tienen la categoría general "Nd" (dígitos decimales) y un Numeric_Type de "Decimal". En este caso, el valor es el valor de dígito decimal del carácter., El carácter es una de las letras latinas mayúsculas `'A'` a `'Z'`. En este caso, el valor es `codepoint - 'A' + 10`., El carácter es una de las letras latinas minúsculas `'a'` a `'z'`. En este caso, el valor es `codepoint - 'a' + 10`., Las letras latinas del rango ASCII (`0061..007A`, `0041..005A`) así como del rango ASCII de ancho completo (`FF41..FF5A`, `FF21..FF3A`) son reconocidas.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

`base`  
La base de numeración (por omisión `10`).

## Valores devueltos

Devuelve el valor numérico representado por el carácter en la base de numeración especificada, o `false` si no hay valor o si el valor excede la base. Devuelve `null` en caso de fallo.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php

var_dump(IntlChar::digit("0"));
var_dump(IntlChar::digit("3"));

var_dump(IntlChar::digit("A", 16));
var_dump(IntlChar::digit("A"));

?>

   
```php

El ejemplo anterior mostrará:

        
    int(0)
    int(3)
    int(10)
    bool(false)

## Véase también

`IntlChar::forDigit`, `IntlChar::charDigitValue`, `IntlChar::isdigit`, `IntlChar::PROPERTY_NUMERIC_TYPE`
