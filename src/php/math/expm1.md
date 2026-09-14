---
title: expm1
description: Devuelve exp($num) - 1, calculado de manera precisa incluso cuando el
  valor del número es cercano a cero
source_url: https://www.php.net/manual/es/function.expm1.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/expm1.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_revision: 6abd858a4
order: 44650
---

expm1

Devuelve

exp(\$num) - 1

, calculado de manera precisa incluso cuando el valor del número es cercano a cero

## Descripción

```php
expm1(float $num): float
```php

`expm1` devuelve el equivalente de `exp($num) - 1` calculado de tal manera que será preciso, incluso si el valor del argumento `num` es cercano a `0`, un caso donde la expresión `exp($num) - 1` no es precisa, debido a la sustracción de dos números casi iguales.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

`e` elevado a la potencia `num`, menos uno.

## Véase también

`log1p`, `exp`
