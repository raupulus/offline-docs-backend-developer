---
title: mt_getrandmax
description: El valor aleatorio más grande posible
source_url: https://www.php.net/manual/es/function.mt-getrandmax.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/functions/mt-getrandmax.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: c174b16ad
order: 67870
---

mt_getrandmax

El valor aleatorio más grande posible

## Descripción

```php
mt_getrandmax(): int
```php

Devuelve el valor aleatorio más grande posible que puede devolver la función `mt_rand` sin argumento, lo que corresponde al valor máximo que puede ser utilizado para su parámetro `max` sin que el resultado sea ampliado (y por lo tanto menos aleatorio).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el valor aleatorio más grande posible devuelto por la función `mt_rand`

## Véase también

`mt_rand`, `mt_srand`, `getrandmax`
