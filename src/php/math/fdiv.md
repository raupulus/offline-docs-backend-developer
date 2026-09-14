---
title: fdiv
description: Divide dos números, según la norma IEEE 754
source_url: https://www.php.net/manual/es/function.fdiv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/fdiv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: true
translation_revision: 2b7eebaaf
order: 44660
---

fdiv

Divide dos números, según la norma IEEE 754

## Descripción

```php
fdiv(float $num1, float $num2): float
```php

Devuelve el resultado en coma flotante de la división de `num1` por `num2`. Si `num2` es cero, entonces uno de los valores `INF`, -`INF`, o `NAN` será devuelto.

Cabe señalar que en las comparaciones, `NAN` nunca será igual (`==`) o idéntico (`===`) a ningún valor, incluyendo a sí mismo.

## Parámetros

`num1`  
El dividendo (numerador)

`num2`  
El divisor

## Valores devueltos

El resultado en coma flotante de `num1`/`num2`

## Ejemplos

Uso de `fdiv`

```
<?php
var_dump(fdiv(5.7, 1.3)); // float(4.384615384615385)
var_dump(fdiv(4, 2)); // float(2)
var_dump(fdiv(1.0, 0.0)); // float(INF)
var_dump(fdiv(-1.0, 0.0)); // float(-INF)
var_dump(fdiv(0.0, 0.0)); // float(NAN)
?>

    
```php

## Véase también

Operador de división [`/`](#language.operators.arithmetic), `fmod`, `fpow`
