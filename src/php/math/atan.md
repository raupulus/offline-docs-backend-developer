---
title: atan
description: Arc tangente
source_url: https://www.php.net/manual/es/function.atan.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/atan.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: abed9056c
order: 44520
---

atan

Arc tangente

## Descripción

```php
atan(float $num): float
```php

Se devuelve el arcotangente de `num`, en radianes. `atan` es la función inversa de `tan`, lo que significa que `$num == tan(atan($num))` para cada valor de `num` que se encuentra en el dominio de la función `atan`.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

El arcotangente de `num`, en radianes.

## Véase también

`tan`, `atanh`, `asin`, `acos`
