---
title: ltrim
description: Elimina los espacios (u otros caracteres) del inicio de un string
source_url: https://www.php.net/manual/es/function.ltrim.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/ltrim.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 27ae0a4a1
order: 88870
---

ltrim

Elimina los espacios (u otros caracteres) del inicio de un string

## Descripción

```php
ltrim(string $string, [string $characters]): string
```php

Elimina los espacios (u otros caracteres) del inicio de un string.

## Parámetros

`string`  
El string de entrada.

`characters`  
Opcionalmente, los caracteres a eliminar también pueden ser especificados utilizando el parámetro `characters`. Basta con listar todos los caracteres que deben ser eliminados. Con `..`, es posible especificar un rango creciente de caracteres.

## Valores devueltos

Esta función devuelve un string con los espacios eliminados al inicio del `string`.

## Ejemplos

Ejemplo con `ltrim`

```
<?php

$text = "\t\tThese are a few words :) ...  ";
$binary = "\x09Example string\x0A";
$hello  = "Hello World";
var_dump($text, $binary, $hello);

print "\n";

$trimmed = ltrim($text);
var_dump($trimmed);

$trimmed = ltrim($text, " \t.");
var_dump($trimmed);

$trimmed = ltrim($hello, "Hdle");
var_dump($trimmed);

// Elimina los caracteres de control ASCII del inicio de $binary
// (de 0 a 31, inclusive)
$clean = ltrim($binary, "\x00..\x1F");
var_dump($clean);

?>

    
```php

El ejemplo anterior mostrará:

    string(32) "        These are a few words :) ...  "
    string(16) "    Example string
    "
    string(11) "Hello World"

    string(30) "These are a few words :) ...  "
    string(30) "These are a few words :) ...  "
    string(7) "o World"
    string(15) "Example string
    "

## Véase también

trim

rtrim
