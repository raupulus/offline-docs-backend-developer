---
title: bin2hex
description: Convierte datos binarios en representación hexadecimal
source_url: https://www.php.net/manual/es/function.bin2hex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/bin2hex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 6330e4d73
order: 88610
---

bin2hex

Convierte datos binarios en representación hexadecimal

## Descripción

```php
bin2hex(string $string): string
```php

Devuelve la cadena `string` cuyos todos los caracteres están representados por su equivalente hexadecimal. La cadena devuelta es una cadena ASCII. La conversión soporta caracteres binarios, y utiliza los bits de mayor peso en primer lugar.

## Parámetros

`string`  
Una `string`.

## Valores devueltos

Devuelve la representación hexadecimal de la cadena proporcionada.

## Ejemplos

Ejemplo con `bin2hex`

```
<?php

$hex = bin2hex('Hello world!');

var_dump($hex);
var_dump(hex2bin($hex));
?>

    
```php

El ejemplo anterior mostrará:

    string(24) "48656c6c6f20776f726c6421"
    string(12) "Hello world!"

## Véase también

`hex2bin`, `pack`
