---
title: min
description: El valor más pequeño
source_url: https://www.php.net/manual/es/function.min.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/min.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44800
---

min

El valor más pequeño

## Descripción

```php
min(mixed $value, mixed ...$values): mixed
```php

Firma alternativa (no soportada con argumentos nombrados):

```php
min(array $value_array): mixed
```

Si el primer y único parámetro es un array, `min` retornará el valor más pequeño contenido en el array. Si el primer parámetro es un entero, una cadena o un número decimal, deben proporcionarse al menos dos parámetros y `min` retornará el más pequeño de estos valores.

> [!NOTE]
> Los valores de diferentes tipos serán comparados utilizando las [reglas de comparación estándar](#language.operators.comparison). Actualmente, una cadena no numérica será comparada con un `int`, como si fuera la valor `0`, pero varias `string` no numéricas serán comparadas de forma alfanumérica. El valor actual retornado será del mismo tipo que el original y ninguna conversión de tipo será aplicada.

> [!CAUTION]
> Tenga cuidado al pasar argumentos con tipos diferentes, ya que `min` puede producir resultados impredecibles.

## Parámetros

`value`  
Cualquier valor [comparable](#language.operators.comparison).

`values`  
Cualquier valor [comparable](#language.operators.comparison).

`value_array`  
Un array que contiene los valores.

## Valores devueltos

La función `min` retorna el valor del parámetro considerado como "inferior" según la comparación estándar. Si varios valores de tipos diferentes son evaluados como iguales (i.e. `0` y `'abc'`), el primero proporcionado a la función será retornado.

## Errores/Excepciones

Si se pasa un array vacío, la función `min` lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `min` ahora lanza una `ValueError` en caso de fallo; previamente, `false` era retornado y un error `E_WARNING` era emitido. |
| 8.0.0 | Como las [ comparaciones entre las cadenas y los números](#migration80.incompatible.core.string-number-comparision) han sido cambiadas, `min` ya no retorna un valor diferente basado en el orden de los argumentos en estos casos. |

## Ejemplos

Ejemplo con `min`

```php
<?php
echo min(2, 3, 1, 6, 7), PHP_EOL;  // 1
echo min(array(2, 4, 5)), PHP_EOL; // 2

// Aquí, comparamos -1 < 0, por lo tanto, -1 es el valor más bajo
echo min('hello', -1), PHP_EOL;    // -1

// Con varios arrays de diferentes tamaños, min retorna el más corto
$val = min(array(2, 2, 2), array(1, 1, 1, 1)); // array(2, 2, 2)
var_dump($val);

// Varios arrays del mismo tamaño son comparados desde la izquierda hacia la derecha,
// por lo tanto, en nuestro ejemplo: 2 == 2, pero 4 < 5
$val = min(array(2, 4, 8), array(2, 5, 1)); // array(2, 4, 8)
var_dump($val);

// Si se proporciona un array y un no-array, el array nunca será retornado
// ya que las comparaciones tratan los arrays como mayores que cualquier valor
$val = min('string', array(2, 5, 7), 42);   // string
var_dump($val);

// Si un argumento es NULL o un booleano, será comparado con
// otras valores utilizando la regla FALSE < TRUE según los otros
// tipos proporcionados. En el ejemplo de abajo, tanto -10 como 10 son tratados
// como valiendo TRUE en la comparación
$val = min(-10, FALSE, 10); // FALSE
var_dump($val);

$val = min(-10, NULL, 10);  // NULL
var_dump($val);

// Por otro lado, 0 es tratado como valiendo FALSE, por lo tanto, es "más pequeño que" TRUE
$val = min(0, TRUE); // 0
var_dump($val);
?>

    
```

## Véase también

`max`, `count`
