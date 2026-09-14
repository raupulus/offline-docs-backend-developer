---
title: trim
description: Elimina los espacios (u otros caracteres) al inicio y al final de un
  string
source_url: https://www.php.net/manual/es/function.trim.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/trim.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 27ae0a4a1
order: 89550
---

trim

Elimina los espacios (u otros caracteres) al inicio y al final de un string

## Descripción

```php
trim(string $string, [string $characters]): string
```php

`trim` retorna el string `string`, después de haber eliminado los caracteres invisibles al inicio y al final del string. Si el segundo parámetro `characters` es omitido, `trim` eliminará los siguientes caracteres:

- `" "`: carácter SP en ASCII `0x20`, un espacio ordinario.

- `"\t"`: carácter HT en ASCII `0x09`, una tabulación.

- `"\n"`: carácter LF en ASCII `0x0A`, un salto de línea (line feed).

- `"\r"`: carácter CR en ASCII `0x0D`, un retorno de carro.

- `"\0"`: carácter NUL en ASCII `0x00`, el octeto NUL.

- `"\v"`: carácter VT en ASCII `0x0B`, una tabulación vertical.

## Parámetros

`string`  
El `string` que será recortado.

`characters`  
Opcionalmente, los caracteres a eliminar también pueden ser especificados utilizando el parámetro `characters`. Basta con listar todos los caracteres que deben ser eliminados. Con `..`, es posible especificar un rango creciente de caracteres.

## Valores devueltos

El string recortado.

## Ejemplos

Ejemplo con `trim`

```
<?php

$text   = "\t\tThese are a few words :) ...  ";
$binary = "\x09Example string\x0A";
$hello  = "Hello World";
var_dump($text, $binary, $hello);

print "\n";

$trimmed = trim($text);
var_dump($trimmed);

$trimmed = trim($text, " \t.");
var_dump($trimmed);

$trimmed = trim($hello, "Hdle");
var_dump($trimmed);

$trimmed = trim($hello, 'HdWr');
var_dump($trimmed);

// Elimina los caracteres de control ASCII al inicio y al final de $binary
// (de 0 a 31 inclusive)
$clean = trim($binary, "\x00..\x1F");
var_dump($clean);

?>

    
```php

El ejemplo anterior mostrará:

    string(32) "        These are a few words :) ...  "
    string(16) "    Example string
    "
    string(11) "Hello World"

    string(28) "These are a few words :) ..."
    string(24) "These are a few words :)"
    string(5) "o Wor"
    string(9) "ello Worl"
    string(14) "Example string"

Eliminación de caracteres en un array con `trim`

```
<?php
function trim_value(&$value)
{
    $value = trim($value);
}

$fruit = array('apple','banana ', ' cranberry ');
var_dump($fruit);

array_walk($fruit, 'trim_value');
var_dump($fruit);

?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      string(5) "apple"
      [1]=>
      string(7) "banana "
      [2]=>
      string(11) " cranberry "
    }
    array(3) {
      [0]=>
      string(5) "apple"
      [1]=>
      string(6) "banana"
      [2]=>
      string(9) "cranberry"
    }

## Notas

> [!NOTE]
> Debido a que la función `trim` elimina caracteres al inicio y al final del string, puede resultar confuso cuando los caracteres son (o no) eliminados desde el medio. `trim('abc', 'bad')` elimina tanto 'a' como 'b' porque la función elimina 'a', luego, mueve 'b' al inicio del string, que también será eliminado. Asimismo, es la razón por la cual la función "funciona" mientras que `trim('abc', 'b')` no funciona.

## Véase también

ltrim

rtrim

str_replace
