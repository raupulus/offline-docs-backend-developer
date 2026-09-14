---
title: IntlChar::charFromName
description: Encuentra un carácter Unicode por su nombre y devuelve su valor de punto
  de código
source_url: https://www.php.net/manual/es/intlchar.charfromname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/charfromname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 40710
---

IntlChar::charFromName

Encuentra un carácter Unicode por su nombre y devuelve su valor de punto de código

## Descripción

```php
public static IntlChar::charFromName(string $name, [int $type]): int
```php

Encuentra un carácter Unicode por su nombre y devuelve su valor de punto de código.

El nombre es comparado exactamente y completamente. Si el nombre no corresponde a un punto de código, `null` es devuelto.

Un nombre Unicode 1.0 es encontrado únicamente si difiere del nombre moderno. Los nombres Unicode están todos en mayúsculas. Los nombres extendidos están en minúsculas seguidos de un número hexadecimal en mayúsculas, y entre chevrons.

## Parámetros

`name`  
El nombre completo del carácter Unicode.

`type`  
Qué nombres utilizar para la búsqueda. Puede ser una de las constantes siguientes: `IntlChar::UNICODE_CHAR_NAME` (por omisión), `IntlChar::UNICODE_10_CHAR_NAME`, `IntlChar::EXTENDED_CHAR_NAME`, `IntlChar::CHAR_NAME_ALIAS`, `IntlChar::CHAR_NAME_CHOICE_COUNT`

## Valores devueltos

El valor Unicode del punto de código con el nombre dado (como `int`), o `null` si no existe tal punto de código.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charFromName("LATIN CAPITAL LETTER A"));
var_dump(IntlChar::charFromName("SNOWMAN"));
var_dump(IntlChar::charFromName("RECYCLING SYMBOL FOR TYPE-1 PLASTICS"));
var_dump(IntlChar::charFromName("A RANDOM STRING WHICH DOESN'T CORRESPOND TO ANY UNICODE CHARACTER"));
?>

   
```php

El ejemplo anterior mostrará:

        
    int(65)
    int(9731)
    int(9843)
    NULL

## Véase también

`IntlChar::charName`, `IntlChar::enumCharNames`
