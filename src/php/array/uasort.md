---
title: uasort
description: Ordena un array utilizando una función de retrollamada
source_url: https://www.php.net/manual/es/function.uasort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/uasort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2226ad08f
order: 5990
---

uasort

Ordena un array utilizando una función de retrollamada

## Descripción

```php
uasort(array $array, callable $callback): true
```php

Ordena `array` en el lugar de tal manera que la correlación entre las claves y los valores sea conservada, utilizando una función de comparación definida por el usuario.

Utilizado habitualmente al ordenar arrays asociativos donde el orden actual de los elementos es significativo.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

> [!NOTE]
> Reinicia el puntero interno del array al primer elemento.

## Parámetros

`array`  
El array de entrada.

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

| Versión | Descripción |
|----|----|
| 8.2.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.0.0 | Si `callback` espera un parámetro a ser pasado por referencia, esta función emite ahora una `E_WARNING`. |

## Ejemplos

Ejemplo con `uasort`

```php
<?php
// Función de comparación
function cmp($a, $b) {
    if ($a == $b) {
        return 0;
    }
    return ($a < $b) ? -1 : 1;
}

// Array a ordenar
$array = array('a' => 4, 'b' => 8, 'c' => -1, 'd' => -9, 'e' => 2, 'f' => 5, 'g' => 3, 'h' => -4);
print_r($array);

// Ordena y muestra el array resultante
uasort($array, 'cmp');
print_r($array);
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [a] => 4
        [b] => 8
        [c] => -1
        [d] => -9
        [e] => 2
        [f] => 5
        [g] => 3
        [h] => -4
    )
    Array
    (
        [d] => -9
        [h] => -4
        [c] => -1
        [e] => 2
        [g] => 3
        [a] => 4
        [f] => 5
        [b] => 8
    )

## Véase también

usort

uksort

Las funciones de

ordenación de arrays
