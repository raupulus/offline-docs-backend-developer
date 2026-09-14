---
title: ctype_space
description: Chequear posibles caracteres de espacio en blanco
source_url: https://www.php.net/manual/es/function.ctype-space.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-space.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8530
---

ctype_space

Chequear posibles caracteres de espacio en blanco

## Descripción

```php
ctype_space(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada, `text`, crean espacios en blanco.

## Parámetros

`text`  
El string de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `text` genera cierto tipo de espacio en blanco, o `false` de lo contrario. Junto con el caracter regular de espacio en blanco, también se consideran espacios a los caracteres de tabulación, tabulación vertical, avance de línea, retorno de carro y avance de formulario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_space`

```
<?php
$cadenas = array(
    'cadena1' => "\n\r\t",
    'cadena2' => "\narf12",
    'cadena3' => '\n\r\t' // observe las comillas simples
);
foreach ($cadenas as $nombre => $caso_prueba) {
    if (ctype_space($caso_prueba)) {
        echo "La cadena '$nombre' contiene únicamente caracteres de espacio en blanco.\n";
    } else {
        echo "La cadena '$nombre' contiene caracteres que no son de espacio en blanco.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena 'cadena1' contiene únicamente caracteres de espacio en blanco.
    La cadena 'cadena2' contiene caracteres que no son de espacio en blanco.
    La cadena 'cadena3' contiene caracteres que no son de espacio en blanco.

## Véase también

`ctype_cntrl`, `ctype_graph`, `ctype_punct`, `IntlChar::isspace`
