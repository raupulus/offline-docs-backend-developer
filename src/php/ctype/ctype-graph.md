---
title: ctype_graph
description: Chequear posibles caracteres imprimibles, con excepción de los espacios
source_url: https://www.php.net/manual/es/function.ctype-graph.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-graph.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8490
---

ctype_graph

Chequear posibles caracteres imprimibles, con excepción de los espacios

## Descripción

```php
ctype_graph(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada, `text`, generan una salida visible.

## Parámetros

`text`  
La cadena de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `texto` es imprimible y genera alguna salida visible (no incluye los espacios), o `false` de lo contrario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_graph`

```
<?php
$cadenas = array('cadena1' => "asdf\n\r\t", 'cadena2' => 'arf12', 'cadena3' => 'LKA#@%.54');
foreach ($cadenas as $nombre => $caso_prueba) {
    if (ctype_graph($caso_prueba)) {
        echo "La cadena '$nombre' consiste completamente de caracteres (visiblemente) imprimibles.\n";
    } else {
        echo "La cadena '$nombre' no consiste completamente de caracteres (visiblemente) imprimibles.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena 'cadena1' no consiste completamente de caracteres (visiblemente) imprimibles.
    La cadena 'cadena2' consiste completamente de caracteres (visiblemente) imprimibles.
    La cadena 'cadena3' consiste completamente de caracteres (visiblemente) imprimibles.

## Véase también

`ctype_alnum`, `ctype_print`, `ctype_punct`, `IntlChar::isgraph`
