---
title: asin
description: Arco seno
source_url: https://www.php.net/manual/es/function.asin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/asin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: abed9056c
order: 44500
---

asin

Arco seno

## Descripción

```php
asin(float $num): float
```php

Se devuelve el arco seno de `num` (`num` en radianes). `asin` es la función inversa de `sin`, lo que significa que `$num == sin(asin($num))` para cada valor de `num` que se encuentra en el dominio de la función `asin`.

## Parámetros

`num`  
El argumento a tratar

## Valores devueltos

El arco seno de `num`, en radianes.

## Véase también

`sin`, `asinh`, `acos`, `atan`
