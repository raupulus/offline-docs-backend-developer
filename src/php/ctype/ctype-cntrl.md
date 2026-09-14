---
title: ctype_cntrl
description: Chequear posibles caracteres de control
source_url: https://www.php.net/manual/es/function.ctype-cntrl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-cntrl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8470
---

ctype_cntrl

Chequear posibles caracteres de control

## Descripción

```php
ctype_cntrl(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada, `text`, son caracteres de control. Los caracteres de control son, por ejemplo, la alimentación de línea, el tabulador, escape.

## Parámetros

`text`  
El string de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter de `texto` es un caracter de control de la localización actual, `false` de lo contrario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_cntrl`

```
<?php
$cadenas = array('cadena1' => "\n\r\t", 'cadena2' => 'arf12');
foreach ($cadenas as $nombre => $caso_prueba) {
    if (ctype_cntrl($caso_prueba)) {
        echo "La cadena '$nombre' consiste completamente de caracteres de control.\n";
    } else {
        echo "La cadena '$nombre' no consiste completamente de caracteres de control.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena 'cadena1' consiste completamente de caracteres de control.
    La cadena 'cadena2' no consiste completamente de caracteres de control.

## Véase también

`ctype_print`, `IntlChar::iscntrl`
