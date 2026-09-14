---
title: ini_parse_quantity
description: Devuelve el tamaño interpretado a partir de la sintaxis abreviada ini
source_url: https://www.php.net/manual/es/function.ini-parse-quantity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/ini-parse-quantity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 4c016ab33
order: 39060
---

ini_parse_quantity

Devuelve el tamaño interpretado a partir de la sintaxis abreviada ini

## Descripción

```php
ini_parse_quantity(string $shorthand): int
```php

Devuelve el tamaño interpretado en bytes en caso de éxito a partir de una [sintaxis abreviada ini](#faq.using.shorthandbytes).

## Parámetros

`shorthand`  
La sintaxis abreviada ini a interpretar, debe ser un número seguido de un multiplicador opcional. Los multiplicadores siguientes son soportados: `k`/`K` (`1024`), `m`/`M` (`1048576`), `g`/`G` (`1073741824`). El número puede ser un decimal, hexadecimal (prefijado por `0x` o `0X`), octal (prefijado por `0o`, `0O` o `0`) o binario (prefijado por `0b` o `0B`)

## Valores devueltos

Devuelve el tamaño interpretado en bytes en tanto que `int`.

## Errores/Excepciones

Si el valor no puede ser interpretado, o si un multiplicador inválido es utilizado, un `E_WARNING` es emitido.

## Ejemplos

Algunos ejemplos de `ini_parse_quantity`

```
<?php

var_dump(ini_parse_quantity('1024'));
var_dump(ini_parse_quantity('1024M'));
var_dump(ini_parse_quantity('512K'));
var_dump(ini_parse_quantity('0xFFk'));
var_dump(ini_parse_quantity('0b1010k'));
var_dump(ini_parse_quantity('0o1024'));
var_dump(ini_parse_quantity('01024'));
var_dump(ini_parse_quantity('Foobar'));
var_dump(ini_parse_quantity('10F'));

?>

    
```php

El ejemplo anterior mostrará:

    int(1024)
    int(1073741824)
    int(524288)
    int(261120)
    int(10240)
    int(532)
    int(532)

    Warning: Invalid quantity "Foobar": no valid leading digits, interpreting as "0" for backwards compatibility
    int(0)

    Warning: Invalid quantity "10F": unknown multiplier "F", interpreting as "10" for backwards compatibility
    int(10)

## Véase también

ini_get
