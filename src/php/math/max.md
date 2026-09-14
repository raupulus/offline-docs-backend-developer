---
title: max
description: El valor más grande
source_url: https://www.php.net/manual/es/function.max.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/max.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44790
---

max

El valor más grande

## Descripción

```php
max(mixed $value, mixed ...$values): mixed
```php

Firma alternativa (no soportada con argumentos nombrados):

```php
max(array $value_array): mixed
```

Si el primer y único parámetro es un array, `max` devuelve el valor más alto del array. Si se proporcionan al menos dos parámetros, `max` devuelve el más grande de estos valores.

> [!NOTE]
> Los valores de diferentes tipos serán comparados utilizando las [reglas de comparación estándar](#language.operators.comparison). Actualmente, un string no numérico será comparado con un `int` como si fuera el valor `0`, pero varios `string` no numéricos serán comparados de forma alfanumérica. El valor actual devuelto será del mismo tipo que el original y no se aplicará ninguna conversión de tipo.

> [!CAUTION]
> Tenga cuidado al pasar argumentos con tipos diferentes, ya que `max` puede producir resultados impredecibles.

## Parámetros

`value`  
Cualquier valor [comparable](#language.operators.comparison).

`values`  
Cualquier valor [comparable](#language.operators.comparison).

`value_array`  
Un array que contiene los valores.

## Valores devueltos

La función `max` devuelve el valor del parámetro considerado como "superior" según la comparación estándar. Si varias valores de tipos diferentes son evaluados como iguales (i.e. `0` y `'abc'`), el primero proporcionado a la función será devuelto.

## Errores/Excepciones

Si se pasa un array vacío, la función `max` lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `max` ahora lanza una `ValueError` en caso de fallo; previamente, `false` era devuelto y se emitía un error `E_WARNING`. |
| 8.0.0 | Como las [ comparaciones entre strings y números](#migration80.incompatible.core.string-number-comparision) han sido cambiadas, `max` ya no devuelve un valor diferente basado en el orden de los argumentos en estos casos. |

## Ejemplos

Ejemplo con `max`

```php
<?php
echo max(2, 3, 1, 6, 7), PHP_EOL;  // 7
echo max(array(2, 4, 5)), PHP_EOL; // 5

// Aquí, comparamos -1 < 0, por lo que 'hello' es el valor más grande
echo max('hello', -1), PHP_EOL;    // hello

// Con varios arrays de diferentes tamaños, max devuelve
// el más largo
$val = max(array(2, 2, 2), array(1, 1, 1, 1)); // array(1, 1, 1, 1)
var_dump($val);

// Varios arrays de la misma longitud son comparados de izquierda a derecha
// también, en nuestro ejemplo: 2 == 2, pero 5 > 4
$val = max(array(2, 4, 8), array(2, 5, 1)); // array(2, 5, 1)
var_dump($val);

// Si se proporciona un array y un no-array, el array será siempre
// devuelto, sabiendo que las comparaciones tratan los arrays como
// más grandes que cualquier valor
$val = max('string', array(2, 5, 7), 42);   // array(2, 5, 7)
var_dump($val);

// Si un argumento es NULL o un booleano, será comparado con otros
// valores utilizando la regla FALSE < TRUE según los otros tipos concernidos
// En el ejemplo de abajo, -10 es tratado como TRUE en la comparación
$val = max(-10, FALSE); // -10
var_dump($val);

// Por otro lado, 0 es tratado como FALSE, por lo que es "más pequeño que" TRUE
$val = max(0, TRUE); // TRUE
var_dump($val);
?>

    
```

## Véase también

`min`, `count`
