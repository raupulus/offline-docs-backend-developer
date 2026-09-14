---
title: log1p
description: Calcula con precisión log(1 + número)
source_url: https://www.php.net/manual/es/function.log1p.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/log1p.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_revision: 0c9c2dd66
order: 44780
---

log1p

Calcula con precisión log(1 + número)

## Descripción

```php
log1p(float $num): float
```php

`log1p` devuelve log(1 + `num`) calculado de tal manera que será preciso incluso si el valor de `num` está próximo a `0`. `log` solo puede devolver log(1) en este caso por falta de precisión.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

log(1 + `num`)

## Véase también

`expm1`, `log`, `log10`
