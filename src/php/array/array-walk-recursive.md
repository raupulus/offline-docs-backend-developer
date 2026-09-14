---
title: array_walk_recursive
description: Aplica una función de retrollamada de manera recursiva a cada miembro
  de un array
source_url: https://www.php.net/manual/es/function.array-walk-recursive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-walk-recursive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: cec5275f2
order: 5710
---

array_walk_recursive

Aplica una función de retrollamada de manera recursiva a cada miembro de un array

## Descripción

```php
array_walk_recursive(array $array, callable $callback, [mixed $arg]): true
```php

Aplica la función de usuario `callback` a cada elemento del array `array`. Esta función se reproducirá en todas las profundidades del array.

## Parámetros

`array`  
El array de entrada.

`callback`  
Típicamente, `callback` toma 2 argumentos. El argumento `array`, representando el valor, es el primero, el índice/clave, el segundo.

> [!NOTE]
> Si `callback` debe ser ejecutado con los valores actuales del array, especifique el primer argumento de `callback` por [referencia](#language.references). Entonces, cualquier cambio efectuado en los elementos de este array será también efectuado en el array original.

`arg`  
Si el argumento opcional `arg` es proporcionado, será pasado como tercer argumento a la función de retrollamada `callback`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `array_walk_recursive`

```
<?php
$sweet = array('a' => 'apple', 'b' => 'banana');
$fruits = array('sweet' => $sweet, 'sour' => 'lemon');

function test_print($item, $key)
{
    echo "La clave $key contiene el elemento $item\n";
}

array_walk_recursive($fruits, 'test_print');
?>

    
```php

El ejemplo anterior mostrará:

```
La clave a contiene el elemento apple
La clave b contiene el elemento banana
La clave sour contiene el elemento lemon

    
```php

Se habrá notado que la clave '`sweet`' nunca es mostrada. Cualquier clave que esté asociada a un `array` no es pasada a la función de retrollamada.

## Véase también

`array_walk`
