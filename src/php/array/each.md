---
title: each
description: Devuelve cada par clave/valor de un array
source_url: https://www.php.net/manual/es/function.each.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/each.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 5790
---

each

Devuelve cada par clave/valor de un array

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0.

## Descripción

```php
each(array $array): array
```php

`each` devuelve el par clave/valor actual del array `array` y avanza el puntero del array.

Tras cada llamada a `each`, el puntero del array se desplaza al siguiente elemento, o más allá del último elemento, cuando se llega al final. Debe utilizarse `reset` si se desea recorrer el array nuevamente con `each`.

## Parámetros

`array`  
El array de entrada.

## Valores devueltos

Devuelve el par clave/valor actual del array `array` y avanza el puntero del array. Este par se devuelve en un array de 4 elementos, con las claves `0`, `1`, `key`, y `value`. Los elementos `0` y `key` contienen el nombre de la clave y `1` y `value` contienen el valor.

Si el puntero interno del array está más allá del final del array, `each` devuelve `false`.

## Ejemplos

Ejemplo con `each`

```
<?php
$foo = array("bob", "fred", "jussi", "jouni", "egon", "marliese");
$bar = each($foo);
print_r($bar);
?>

    
```php

`$bar` contiene ahora las claves/valores siguientes :

    Array
    (
        [1] => bob
        [value] => bob
        [0] => 0
        [key] => 0
    )

```
<?php
$foo = array("Robert" => "Bob", "Seppo" => "Sepi");
$bar = each($foo);
print_r($bar);
?>

    
```php

`$bar` contiene ahora las claves/valores siguientes :

    Array
    (
        [1] => Bob
        [value] => Bob
        [0] => Robert
        [key] => Robert
    )

`each` se utiliza típicamente en conjunción con `list` para revisar un array. Por ejemplo :

Recorrer un array con `each`

```
<?php
$fruit = array('a' => 'apple', 'b' => 'banana', 'c' => 'cranberry');

reset($fruit);
while (list($key, $val) = each($fruit)) {
    echo "$key => $val\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    a => apple
    b => banana
    c => cranberry

> [!CAUTION]
> Asignar un array a otra variable reinicia el puntero del array original a cero. Debido a este comportamiento, se podría haber provocado una iteración infinita en nuestro ejemplo si se hubiera asignado `$fruit` a otra variable dentro de nuestro ciclo.

> [!WARNING]
> `each` también acepta objetos, pero puede devolver un resultado no esperado. Por lo tanto, no se recomienda utilizar esta función con objetos.

## Véase también

`key`, `list`, `current`, `reset`, `next`, `prev`, [`foreach`](#control-structures.foreach), [Iteración de objetos](#language.oop5.iterations)
