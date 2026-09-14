---
title: array_product
description: Calcula el producto de los valores del array
source_url: https://www.php.net/manual/es/function.array-product.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-product.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 443d81b33
order: 5500
---

array_product

Calcula el producto de los valores del array

## Descripción

```php
array_product(array $array): int
```php

`array_product` devuelve el producto de los valores del array `array`.

## Parámetros

`array`  
El array.

## Valores devueltos

Devuelve el producto, en forma de `int` o de `float`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Emite ahora un `E_WARNING` cuando los valores de tipo `array` no pueden ser convertidos en `int` o `float`. Anteriormente, los arrays y los objetos eran ignorados mientras que todos los demás valores eran convertidos en `int`. Además, los objetos que definen una conversión numérica (por ejemplo, `GMP`) son ahora convertidos en lugar de ser ignorados. |

## Ejemplos

Ejemplo con `array_product`

```
<?php

$a = array(2, 4, 6, 8);
echo "producto(a) = " . array_product($a) . "\n";
echo "producto(array()) = " . array_product(array()) . "\n";

?>

    
```php

El ejemplo anterior mostrará:

    producto(a) = 384
    producto(array()) = 1
