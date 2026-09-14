---
title: IntlChar::forDigit
description: Devuelve la representación de carácter para un dígito dado y una base
  de numeración
source_url: https://www.php.net/manual/es/intlchar.fordigit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/fordigit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: a3f969dec
order: 40800
---

IntlChar::forDigit

Devuelve la representación de carácter para un dígito dado y una base de numeración

## Descripción

```php
public static IntlChar::forDigit(int $digit, [int $base]): int
```php

Determina la representación de carácter para un dígito específico en la base de numeración especificada.

Si el valor de la base de numeración no es una base de numeración válida, o si el valor del dígito no es un dígito válido en la base especificada, se devuelve el carácter nulo (`U+0000`).

La base de numeración es válida si es superior o igual a `2` e inferior o igual a `36`. El valor del dígito es válido si `0 <= dígito < base`.

Si el dígito es inferior a `10`, entonces '0' + dígito es devuelto. De lo contrario, se devuelve el valor 'a' + dígito - 10.

## Parámetros

`digit`  
El dígito a convertir en carácter.

`base`  
La base de numeración (por omisión `10`).

## Valores devueltos

El carácter representativo (en forma de `int`) del dígito especificado en la base de numeración especificada.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::forDigit(0));
var_dump(IntlChar::forDigit(3));
var_dump(IntlChar::forDigit(3, 10));
var_dump(IntlChar::forDigit(10));
var_dump(IntlChar::forDigit(10, 16));
?>

   
```php

El ejemplo anterior mostrará:

        
    int(48)
    int(51)
    int(51)
    int(0)
    int(97)

## Véase también

`IntlChar::digit`, `IntlChar::charDigitValue`, `IntlChar::isdigit`, `IntlChar::PROPERTY_NUMERIC_TYPE`
