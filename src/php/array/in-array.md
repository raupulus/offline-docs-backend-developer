---
title: in_array
description: Indica si un valor pertenece a un array
source_url: https://www.php.net/manual/es/function.in-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/in-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 2e60c5134
order: 5820
---

in_array

Indica si un valor pertenece a un array

## Descripción

```php
in_array(mixed $needle, array $haystack, [bool $strict]): bool
```php

Busca `needle` en `haystack` utilizando una comparación flexible a menos que `strict` sea utilizado.

## Parámetros

`needle`  
El valor buscado.

> [!NOTE]
> Si `needle` es un `string`, la comparación se realiza teniendo en cuenta la casilla.

`haystack`  
El array.

`strict`  
Si el tercer argumento `strict` está definido a `true` entonces la función `in_array` verificará también que el [tipo](#language.types) del argumento `needle` coincide con el tipo del valor encontrado en `haystack`.

> [!NOTE]
> Antes de PHP 8.0.0, un `string` `needle` coincidirá con un valor de array de `0` en modo no estricto y viceversa. Esto puede llevar a resultados no deseados. Casos similares también existen para otros tipos. Si no se está absolutamente seguro de los tipos de valores involucrados, siempre se debe utilizar el flag `strict` para evitar cualquier comportamiento inesperado.

## Valores devueltos

Devuelve `true` si `needle` es encontrado en el array, `false` en caso contrario.

## Ejemplos

Ejemplo con `in_array`

```
<?php
$os = array("Mac", "NT", "Irix", "Linux");
if (in_array("Irix", $os)) {
    echo "Got Irix";
}
if (in_array("mac", $os)) {
    echo "Got mac";
}
?>

    
```php

La segunda condición falla, ya que `in_array` es sensible a la casilla. El script devuelve:

    Got Irix

Ejemplo con `in_array` y modo estricto

```
<?php
$a = array('1.10', 12.4, 1.13);

if (in_array('12.4', $a, true)) {
    echo "'12.4' es encontrado con modo estricto\n";
}

if (in_array(1.13, $a, true)) {
    echo "1.13 es encontrado con modo estricto\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    1.13 es encontrado con modo estricto

Ejemplo con `in_array` y un array como argumento

```
<?php
$a = array(array('p', 'h'), array('p', 'r'), 'o');

if (in_array(array('p', 'h'), $a)) {
    echo "'ph' ha sido encontrado\n";
}

if (in_array(array('f', 'i'), $a)) {
    echo "'fi' ha sido encontrado\n";
}

if (in_array('o', $a)) {
    echo "'o' ha sido encontrado\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    'ph' ha sido encontrado
    'o' ha sido encontrado

## Véase también

`array_search`, `isset`, `array_key_exists`
