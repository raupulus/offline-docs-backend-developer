---
title: IntlChar::charName
description: Devuelve el nombre de un carácter Unicode
source_url: https://www.php.net/manual/es/intlchar.charname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/charname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 40730
---

IntlChar::charName

Devuelve el nombre de un carácter Unicode

## Descripción

```php
public static IntlChar::charName(int $codepoint, [int $type]): string
```php

Devuelve el nombre de un carácter Unicode.

Según el `type`, el nombre del carácter es el nombre "moderno" o el nombre que fue definido en la versión Unicode 1.0. El nombre contiene solo caracteres "invariantes" como A-Z, 0-9, espacio y '-'. Los nombres Unicode 1.0 solo se recuperan si son diferentes de los nombres modernos y si ICU contiene los datos para ellos.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

`type`  
Qué nombres utilizar para la búsqueda. Puede ser una de las constantes siguientes: `IntlChar::UNICODE_CHAR_NAME` (por omisión), `IntlChar::UNICODE_10_CHAR_NAME`, `IntlChar::EXTENDED_CHAR_NAME`, `IntlChar::CHAR_NAME_ALIAS`, `IntlChar::CHAR_NAME_CHOICE_COUNT`

## Valores devueltos

El valor correspondiente, o una cadena vacía si no hay nombre para ese carácter, o `null` si no hay punto de código.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charName("."));
var_dump(IntlChar::charName(".", IntlChar::UNICODE_CHAR_NAME));
var_dump(IntlChar::charName("\u{2603}"));
var_dump(IntlChar::charName("\u{0000}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(9) "FULL STOP"
    string(9) "FULL STOP"
    string(7) "SNOWMAN"
    string(0) ""

## Véase también

`IntlChar::charFromName`, `IntlChar::enumCharNames`
