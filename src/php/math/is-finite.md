---
title: is_finite
description: Verifica si un número flotante es finito
source_url: https://www.php.net/manual/es/function.is-finite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/is-finite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: f940d0cf4
order: 44730
---

is_finite

Verifica si un número flotante es finito

## Descripción

```php
is_finite(float $num): bool
```php

Retorna si el `num` dado es un número flotante finito.

Un número flotante finito no es ni `NAN` (`is_nan`), ni infinito (`is_infinite`).

## Parámetros

`num`  
El `float` a verificar

## Valores devueltos

`true` si `num` no es ninguno de `NAN`, `INF`, -`INF`, de lo contrario `false`.

## Ejemplos

Ejemplo de `is_finite`

```
<?php
$float = 1.2345;
var_dump($float, is_finite($float));

$nan = sqrt(-1);
var_dump($nan, is_finite($nan));

$inf = 1e308 * 2;
var_dump($inf, is_finite($inf));
?>

    
```php

El ejemplo anterior mostrará:

    float(1.2345)
    bool(true)
    float(NAN)
    bool(false)
    float(INF)
    bool(false)

## Véase también

`is_infinite`, `is_nan`
