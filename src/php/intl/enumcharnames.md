---
title: IntlChar::enumCharNames
description: Enumera todos los caracteres Unicode asignados en un rango
source_url: https://www.php.net/manual/es/intlchar.enumcharnames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/enumcharnames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 40770
---

IntlChar::enumCharNames

Enumera todos los caracteres Unicode asignados en un rango

## Descripción

```php
public static IntlChar::enumCharNames(int $start, int $end, callable $callback, [int $type]): bool
```php

Enumera todos los caracteres Unicode asignados entre los puntos de código de inicio y fin (inclusive el inicio, exclusivo el fin) y llama a una función para cada uno, pasando el valor del punto de código y el nombre del carácter.

Para los nombres Unicode 1.0, solo aquellos que difieren de los nombres modernos son enumerados.

## Parámetros

`start`  
El primer punto de código en el rango de enumeración.

`end`  
Un o más puntos de código adicionales al último punto de código en el rango de enumeración (el primero después del rango).

`callback`  
La función que debe ser llamada para cada nombre de carácter. Los tres argumentos siguientes le serán pasados: `int` `$codepoint` - El valor numérico del punto de código, `int` `$nameChoice` - El mismo valor que el parámetro `type` a continuación, `string` `$name` - El nombre del carácter

`type`  
Un selector para el tipo de nombres a enumerar. Puede ser una de las constantes siguientes: `IntlChar::UNICODE_CHAR_NAME` (por omisión), `IntlChar::UNICODE_10_CHAR_NAME`, `IntlChar::EXTENDED_CHAR_NAME`, `IntlChar::CHAR_NAME_ALIAS`, `IntlChar::CHAR_NAME_CHOICE_COUNT`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Este método devuelve ahora `false` en caso de fallo; previamente devolvía `null`. |

## Ejemplos

Enumera un rango de ejemplos de puntos de código

```
    
<?php
IntlChar::enumCharNames(0x2600, 0x2610, function($codepoint, $nameChoice, $name) {
    printf("U+%04x %s\n", $codepoint, $name);
});
?>

   
```php

El ejemplo anterior mostrará:

        
    U+2600 BLACK SUN WITH RAYS
    U+2601 CLOUD
    U+2602 UMBRELLA
    U+2603 SNOWMAN
    U+2604 COMET
    U+2605 BLACK STAR
    U+2606 WHITE STAR
    U+2607 LIGHTNING
    U+2608 THUNDERSTORM
    U+2609 SUN
    U+260a ASCENDING NODE
    U+260b DESCENDING NODE
    U+260c CONJUNCTION
    U+260d OPPOSITION
    U+260e BLACK TELEPHONE
    U+260f WHITE TELEPHONE

## Véase también

`IntlChar::charName`, `IntlChar::charFromName`
