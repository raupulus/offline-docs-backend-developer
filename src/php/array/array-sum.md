---
title: array_sum
description: Calcula la suma de los valores del array
source_url: https://www.php.net/manual/es/function.array-sum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-sum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 443d81b33
order: 5610
---

array_sum

Calcula la suma de los valores del array

## Descripción

```php
array_sum(array $array): int
```php

`array_sum` devuelve la suma de los valores del array `array`.

## Parámetros

`array`  
El array de entrada.

## Valores devueltos

Devuelve la suma de los valores, en forma de un `int` o de un `float` `0` si el `array` está vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Emite ahora un `E_WARNING` cuando los valores de tipo `array` no pueden ser convertidos en `int` o `float`. Anteriormente, los arrays y los objetos eran ignorados mientras que todos los demás valores eran convertidos en `int`. Además, los objetos que definen una conversión numérica (por ejemplo, `GMP`) son ahora convertidos en lugar de ser ignorados. |

## Ejemplos

Ejemplo con `array_sum`

```
<?php
$a = array(2, 4, 6, 8);
echo "sum(a) = " . array_sum($a) . "\n";

$b = array("a" => 1.2, "b" => 2.3, "c" => 3.4);
echo "sum(b) = " . array_sum($b) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    sum(a) = 20
    sum(b) = 6.9
