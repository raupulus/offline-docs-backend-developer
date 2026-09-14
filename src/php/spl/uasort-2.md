---
title: ArrayObject::uasort
description: Ordena los elementos con una función de usuario
source_url: https://www.php.net/manual/es/arrayobject.uasort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/uasort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81540
---

ArrayObject::uasort

Ordena los elementos con una función de usuario

## Descripción

```php
public ArrayObject::uasort(callable $callback): true
```php

Esta función ordena los elementos manteniendo su correlación con la clave asociada, utilizando una función de comparación de usuario.

Esta función se utiliza al ordenar arrays asociativos, donde el orden de los elementos es importante.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

## Parámetros

`callback`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `ArrayObject::uasort`

```php
<?php
// Función de comparación
function cmp($a, $b) {
    if ($a == $b) {
        return 0;
    }
    return ($a < $b) ? -1 : 1;
}

// Los arrays a ordenar
$array = array('a' => 4, 'b' => 8, 'c' => -1, 'd' => -9, 'e' => 2, 'f' => 5, 'g' => 3, 'h' => -4);
$arrayObject = new ArrayObject($array);
var_dump($arrayObject);

// Ordena y muestra el array
$arrayObject->uasort('cmp');
var_dump($arrayObject);
?>

    
```

El ejemplo anterior mostrará:

    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(8) {
        ["a"]=>
        int(4)
        ["b"]=>
        int(8)
        ["c"]=>
        int(-1)
        ["d"]=>
        int(-9)
        ["e"]=>
        int(2)
        ["f"]=>
        int(5)
        ["g"]=>
        int(3)
        ["h"]=>
        int(-4)
      }
    }
    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(8) {
        ["d"]=>
        int(-9)
        ["h"]=>
        int(-4)
        ["c"]=>
        int(-1)
        ["e"]=>
        int(2)
        ["g"]=>
        int(3)
        ["a"]=>
        int(4)
        ["f"]=>
        int(5)
        ["b"]=>
        int(8)
      }
    }

## Véase también

ArrayObject::asort, ArrayObject::ksort, ArrayObject::natsort, ArrayObject::natcasesort, ArrayObject::uksort, `uasort`
