---
title: hypot
description: Calcula la longitud de la hipotenusa de un triángulo rectángulo
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/hypot.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 6406cc6c5
order: 44710
---

hypot

Calcula la longitud de la hipotenusa de un triángulo rectángulo

## Descripción

```php
hypot(float $x, float $y): float
```php

`hypot` devuelve la longitud de la hipotenusa de un triángulo rectángulo que tiene lados de longitud `x` y `y` o bien la distancia del punto (`x`, `y`) desde el origen. Esto es equivalente a `sqrt($x*$x + $y*$y)`.

## Parámetros

`x`  
Longitud del primer lado

`y`  
Longitud del segundo lado

## Valores devueltos

La longitud calculada de la hipotenusa
