---
title: ctype_punct
description: Chequear posibles caracteres imprimibles que no son ni espacios en blanco
  ni caracteres alfanuméricos
source_url: https://www.php.net/manual/es/function.ctype-punct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-punct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8520
---

ctype_punct

Chequear posibles caracteres imprimibles que no son ni espacios en blanco ni caracteres alfanuméricos

## Descripción

```php
ctype_punct(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada, `text`, son caracteres de puntuación.

## Parámetros

`text`  
La cadena de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `text` es imprimible, pero no es una letra, dígito o espacio en blanco; o `false` de lo contrario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_punct`

```
<?php
$cadenas = array('ABasdk!@!$#', '!@ # $', '*&$()');
foreach ($cadenas as $caso_prueba) {
    if (ctype_punct($caso_prueba)) {
        echo "La cadena $caso_prueba consiste completamente de signos de puntuación.\n";
    } else {
        echo "La cadena $caso_prueba no consiste completamente de signos de puntuación.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena ABasdk!@!$# no consiste completamente de signos de puntuación.
    La cadena !@ # $ no consiste completamente de signos de puntuación.
    La cadena *&$() consiste completamente de signos de puntuación.

## Véase también

`ctype_cntrl`, `ctype_graph`, `IntlChar::ispunct`
