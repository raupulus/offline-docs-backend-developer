---
title: acos
description: Arc coseno
source_url: https://www.php.net/manual/es/function.acos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/acos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: abed9056c
order: 44480
---

acos

Arc coseno

## Descripción

```php
acos(float $num): float
```php

Devuelve el arc coseno de `num`. `acos` es la función inversa de `cos`, lo que significa que `$num == cos(acos($num))` para cada valor de `num` que se encuentra en el dominio de la función `acos`.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

El arc coseno de `num`, en radianes.

## Véase también

`cos`, `acosh`, `asin`, `atan`
