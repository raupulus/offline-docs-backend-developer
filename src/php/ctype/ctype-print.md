---
title: ctype_print
description: Chequear posibles caracteres imprimibles
source_url: https://www.php.net/manual/es/function.ctype-print.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-print.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8510
---

ctype_print

Chequear posibles caracteres imprimibles

## Descripción

```php
ctype_print(mixed $text): bool
```php

verifica si todos los caracteres en la `string` entregada, `text`, son imprimibles.

## Parámetros

`text`  
La cadena de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `texto` genera realmente alguna salida (incluyendo los espacios). Devuelve `false` si el `texto` incluye caracteres de control o caracteres que no producen ninguna salida ni realizan función de control alguna después de todo. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_print`

```
<?php
$cadenas = array('cadena1' => "asdf\n\r\t", 'cadena2' => 'arf12', 'cadena3' => 'LKA#@%.54');
foreach ($cadenas as $nombre => $caso_prueba) {
    if (ctype_print($caso_prueba)) {
        echo "La cadena '$nombre' consiste completamente de caracteres imprimibles.\n";
    } else {
        echo "La cadena '$nombre' no consiste completamente de caracteres imprimibles.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena 'cadena1' no consiste completamente de caracteres imprimibles.
    La cadena 'cadena2' consiste completamente de caracteres imprimibles.
    La cadena 'cadena3' consiste completamente de caracteres imprimibles.

## Véase también

`ctype_cntrl`, `ctype_graph`, `ctype_punct`, `IntlChar::isprint`
