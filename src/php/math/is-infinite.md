---
title: is_infinite
description: Verifica si un número de tipo float es infinito
source_url: https://www.php.net/manual/es/function.is-infinite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/is-infinite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: f940d0cf4
order: 44740
---

is_infinite

Verifica si un número de tipo float es infinito

## Descripción

```php
is_infinite(float $num): bool
```php

Indica si el `num` proporcionado es `INF` o -`INF`.

## Parámetros

`num`  
El `float` a verificar

## Valores devueltos

Indica si el `num` proporcionado es `INF` o -`INF`, en caso contrario, `false`.

## Ejemplos

Ejemplo de `is_infinite`

```
<?php
$inf = 1e308 * 2;

var_dump($inf, is_infinite($inf));

$negative_inf = -$inf;

var_dump($negative_inf, is_infinite($negative_inf));
?>

    
```php

El ejemplo anterior mostrará:

    float(INF)
    bool(true)
    float(-INF)
    bool(true)

## Véase también

`is_finite`, `is_nan`
