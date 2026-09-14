---
title: fpow
description: Eleva un número a la potencia de otro, según la norma IEEE 754
source_url: https://www.php.net/manual/es/function.fpow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/fpow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: true
translation_revision: 2b7eebaaf
order: 44690
---

fpow

Eleva un número a la potencia de otro, según la norma IEEE 754

## Descripción

```php
fpow(float $num, float $exponent): float
```php

Devuelve el resultado en coma flotante de la elevación de `num` a la potencia `exponent`. Si `num` es cero y `exponent` es menor que cero, entonces `INF` es devuelto.

## Parámetros

`num`  
La base a utilizar.

`exponent`  
El exponente.

## Valores devueltos

Devuelve un `float` correspondiente a `$num$exponent`.

## Ejemplos

Ejemplo de `fpow`

```
<?php
var_dump(fpow(10, 2));
var_dump(fpow(0, -3));
var_dump(fpow(-1, 5.5));
?>

   
```php

El ejemplo anterior mostrará:

    float(100)
    float(INF)
    float(NAN)

## Véase también

El operador de exponenciación

\*\*

pow

fdiv

fmod
