---
title: rtrim
description: Elimina los espacios (u otros caracteres) al final de un string
source_url: https://www.php.net/manual/es/function.rtrim.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/rtrim.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 27ae0a4a1
order: 89020
---

rtrim

Elimina los espacios (u otros caracteres) al final de un string

## Descripción

```php
rtrim(string $string, [string $characters]): string
```php

Esta función devuelve un string con los espacios (u otros caracteres) eliminados al final de `string`.

Sin el segundo parámetro, `rtrim` eliminará estos caracteres:

- `" "`: carácter SP en ASCII `0x20`, un espacio ordinario.

- `"\t"`: carácter HT en ASCII `0x09`, una tabulación.

- `"\n"`: carácter LF en ASCII `0x0A`, un salto de línea (line feed).

- `"\r"`: carácter CR en ASCII `0x0D`, un retorno de carro.

- `"\0"`: carácter NUL en ASCII `0x00`, el octeto NUL.

- `"\v"`: carácter VT en ASCII `0x0B`, una tabulación vertical.

## Parámetros

`string`  
El string de entrada.

`characters`  
Opcionalmente, los caracteres a eliminar también pueden ser especificados utilizando el parámetro `characters`. Basta con listar todos los caracteres que deben ser eliminados. Con `..`, es posible especificar un rango creciente de caracteres.

## Valores devueltos

Devuelve el string modificado.

## Ejemplos

Ejemplo de uso de `rtrim`

```
<?php

$text = "\t\tAquí hay algunas palabras :) ...  ";
$binary = "\x09String de ejemplo\x0A";
$hello  = "Hola Mundo";
var_dump($text, $binary, $hello);

print "\n";

$trimmed = rtrim($text);
var_dump($trimmed);

$trimmed = rtrim($text, " \t.");
var_dump($trimmed);

$trimmed = rtrim($hello, "Hdlor");
var_dump($trimmed);

// elimina los caracteres de control ASCII al final de $binary
// (de 0 a 31 inclusive)
$clean = rtrim($binary, "\x00..\x1F");
var_dump($clean);

?>

    
```php

El ejemplo anterior mostrará:

    string(32) "        Aquí hay algunas palabras :) ...  "
    string(16) "    String de ejemplo
    "
    string(10) "Hola Mundo"

    string(30) "        Aquí hay algunas palabras :) ..."
    string(26) "        Aquí hay algunas palabras :)"
    string(6) "Hola M"
    string(15) "    String de ejemplo"

## Véase también

trim

ltrim
