---
title: range
description: Crea un array que contiene un intervalo de elementos
source_url: https://www.php.net/manual/es/function.range.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/range.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 647d5c50e
order: 5930
---

range

Crea un array que contiene un intervalo de elementos

## Descripción

```php
range(string $start, string $end, [int $step]): array
```php

Crea un array que contiene un intervalo de elementos.

Si tanto `start` como `end` son `string`, y `step` es de tipo `int`, el array producido será una secuencia de bytes. De lo contrario, el array producido será una secuencia de números.

La secuencia es creciente si `start` es menor o igual a `end`. De lo contrario, la secuencia es decreciente.

## Parámetros

`start`  
Primer valor de la secuencia.

`end`  
Último valor posible de la secuencia.

`step`  
`step` indica de cuánto progresa la secuencia producida entre los valores de la secuencia.

`step` puede ser negativo para las secuencias decrecientes.

Si `step` es un `float` sin parte fraccionaria, se interpreta como un `int`.

## Valores devueltos

Devuelve una secuencia de elementos en forma de un array `array` con el primer elemento siendo `start` hasta `end`, cada valor de la secuencia estando separado por `step` valores.

El último elemento del array devuelto es `end` o el elemento anterior de la secuencia, dependiendo del valor de `step`.

Si tanto `start` como `end` son `string`, y `step` es de tipo `int` el array producido será una secuencia de bytes, generalmente caracteres ASCII latinos.

Si al menos uno de `start`, `end` o `step` es de tipo `float`, el array producido será una secuencia de `float`.

De lo contrario, el array producido será una secuencia de `int`.

## Errores/Excepciones

- Si `step` es igual a `0`, se genera una `ValueError`.

- Si `start`, `end`, o `step` no son `is_finite`, se genera una `ValueError`.

- Si `step` es negativo, pero la plage producida es creciente (es decir, `$start <= $end`), se genera una `ValueError`.

- Si `start` o `end` es la cadena vacía `''`, se emite un `E_WARNING` y la cadena vacía se interpretará como `0`.

- Si `start` o `end` es una cadena no-[numérica](#language.types.numeric-strings) con más de un byte, se emite un `E_WARNING`.

- Si `start` o `end` es una cadena que se convierte implícitamente en `int` porque el otro valor límite es un número, se emite un `E_WARNING`.

- Si `step` es de tipo `float`, y `start` y `end` son cadenas no-[numéricas](#language.types.numeric-strings), se emite un `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Si tanto `start` como `end` son cadenas, entonces `range` producirá ahora sistemáticamente un array de `string`. Anteriormente, si uno de los valores límite era una cadena numérica, el otro valor límite se convertía implícitamente en `int`. |
| 8.3.0 | Ahora se emite un `E_WARNING` si `start` o `end` es una cadena que se convierte implícitamente en `int` porque el otro valor límite es un número. |
| 8.3.0 | Ahora se emite un `E_WARNING` si `start` o `end` es una cadena no-numérica con más de un byte. |
| 8.3.0 | Ahora se emite un `E_WARNING` si `start` o `end` es la cadena vacía. |
| 8.3.0 | Si `step` es de tipo `float` sin parte fraccionaria, se interpretará como un `int`. |
| 8.3.0 | Ahora se genera una `ValueError` si `step` es negativo al producir una plage creciente. |
| 8.3.0 | Ahora se genera una `ValueError` si `step` no es finito. |
| 8.3.0 | Ahora se genera una `TypeError` si `start` o `end` es un array, un objeto, o un recurso. Anteriormente, se convertían implícitamente en `int`. |

## Ejemplos

Ejemplo con `range`

```
<?php
echo implode(', ', range(0, 12)), PHP_EOL;

echo implode(', ', range(0, 100, 10)), PHP_EOL;

echo implode(', ', range('a', 'i')), PHP_EOL;

echo implode(', ', range('c', 'a')), PHP_EOL;

echo implode(', ', range('A', 'z')), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    a, b, c, d, e, f, g, h, i
    c, b, a
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, [, \, ], ^, _, `, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

## Véase también

`shuffle`, `array_fill`, [`foreach`](#control-structures.foreach)
