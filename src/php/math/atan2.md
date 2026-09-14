---
title: atan2
description: Arco tangente de dos variables
source_url: https://www.php.net/manual/es/function.atan2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/atan2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_revision: 96c9d88ba
order: 44530
---

atan2

Arco tangente de dos variables

## Descripción

```php
atan2(float $y, float $x): float
```php

Esta función calcula el arco tangente de las dos variables `x` y `y`. Es similar a calcular el arco tangente de `y` / `x`, excepto que los signos de ambos argumentos son usados para determinar el cuadrante del resultado.

La función devuelve el resultado en radianes, que se encuentra entre -PI y PI (inclusive).

## Parámetros

`y`  
Parámetro dividendo

`x`  
Parámetro divisor

## Valores devueltos

El arco tangente de `y`/`x` en radianes.

## Véase también

`atan`
