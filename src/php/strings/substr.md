---
title: substr
description: Devuelve un segmento de string
source_url: https://www.php.net/manual/es/function.substr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/substr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 71166b721
order: 89540
---

substr

Devuelve un segmento de string

## Descripción

```php
substr(string $string, int $offset, [int $length]): string
```php

Devuelve el segmento de `string` definido por `offset` y `length`.

## Parámetros

`string`  
El string de entrada.

`offset`  
Si `offset` es positivo, el string devuelto comenzará en el carácter número `offset`, en el string `string`. El primer carácter está numerado cero. En efecto, en el string '`abcdef`', el carácter en la posición `0` es '`a`', el carácter en la posición `2` es '`c`', y así sucesivamente.

Si `offset` es negativo, el string devuelto comenzará en el carácter número `offset` contando desde el final del string `string`.

Si `string` es más pequeño que `offset` caracteres de largo, se devolverá un string vacío.

Ejemplo con `offset` negativo

```
<?php
$rest = substr("abcdef", -1), PHP_EOL;    // devuelve "f"
$rest = substr("abcdef", -2), PHP_EOL;    // devuelve "ef"
$rest = substr("abcdef", -3, 1), PHP_EOL; // devuelve "d"
?>

        
```php

`length`  
Si `length` es proporcionado y es positivo, el string devuelto contendrá como máximo `length` caracteres, comenzando desde el carácter `offset` (dependiendo del tamaño del string `string`).

Si se proporciona `length` y es negativo, se omitirá esa cantidad de caracteres al final de `string`. Si `offset` representa una posición de este truncamiento o fuera del string, se devolverá una cadena vacía.

Si el parámetro `length` es proporcionado y vale `0`, se devolverá un string vacío.

Si `length` es omitido o `null`, el substring comenzando desde `offset` hasta el final será devuelto.

Uso de un valor negativo para `length`

```
<?php
$rest = substr("abcdef", 0, -1), PHP_EOL;  // devuelve "abcde"
$rest = substr("abcdef", 2, -1), PHP_EOL;  // devuelve "cde"
$rest = substr("abcdef", 4, -4), PHP_EOL;  // devuelve ""; anterior a PHP 8.0.0, false era devuelto
$rest = substr("abcdef", -3, -1), PHP_EOL; // devuelve "de"
?>

       
```php

## Valores devueltos

Devuelve la parte extraída del string `string`, o un string vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `length` es ahora nullable. Cuando `length` es explícitamente definido como `null`, la función devuelve un substring terminando al final del string, mientras que anteriormente devolvía un string vacío. |
| 8.0.0 | Esta función devuelve un string vacío donde anteriormente devolvía `false` |

## Ejemplos

Ejemplo con `substr`

```
<?php
echo substr('abcdef', 1), PHP_EOL;     // bcdef
echo substr("abcdef", 1, null), PHP_EOL; // bcdef; anterior a PHP 8.0.0, un string vacío era devuelto
echo substr('abcdef', 1, 3), PHP_EOL;  // bcd
echo substr('abcdef', 0, 4), PHP_EOL;  // abcd
echo substr('abcdef', 0, 8), PHP_EOL;  // abcdef
echo substr('abcdef', -1, 1), PHP_EOL; // f

// Acceder a un simple carácter en un string
// también puede ser realizado usando corchetes
$string = 'abcdef';
echo $string[0], PHP_EOL;                 // a
echo $string[3], PHP_EOL;                 // d
echo $string[strlen($string)-1], PHP_EOL; // f

?>

    
```php

Comportamiento del cast con `substr`

```
<?php
class apple {
    public function __toString() {
        return "green";
    }
}

echo "1) ", var_export(substr("pear", 0, 2), true), PHP_EOL;
echo "2) ", var_export(substr(54321, 0, 2), true), PHP_EOL;
echo "3) ", var_export(substr(new apple(), 0, 2), true), PHP_EOL;
echo "4) ", var_export(substr(true, 0, 1), true), PHP_EOL;
echo "5) ", var_export(substr(false, 0, 1), true), PHP_EOL;
echo "6) ", var_export(substr("", 0, 1), true), PHP_EOL;
echo "7) ", var_export(substr(1.2e3, 0, 4), true), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    1) 'pe'
    2) '54'
    3) 'gr'
    4) '1'
    5) ''
    6) ''
    7) '1200'

Intervalo de caracteres inválido

Si un intervalo de caracteres inválido es solicitado, `substr` devuelve un string vacío a partir de PHP 8.0.0; anteriormente `false` era devuelto en su lugar.

```
<?php
var_dump(substr('a', 2));
?>

   
```php

Resultado del ejemplo anterior en PHP 8:

    string(0) ""

       

Resultado del ejemplo anterior en PHP 7:

    bool(false)

## Véase también

`strrchr`, `substr_replace`, `preg_match`, `trim`, `mb_substr`, `wordwrap`, [Acceso y modificación de un string, por carácter](#language.types.string.substr)
