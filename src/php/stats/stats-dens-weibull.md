---
title: stats_dens_weibull
description: La función de densidad de probabilidad de la distribución de Weibull
source_url: https://www.php.net/manual/es/function.stats-dens-weibull.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-weibull.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87130
---

stats_dens_weibull

La función de densidad de probabilidad de la distribución de Weibull

## Descripción

```php
stats_dens_weibull(float $x, float $a, float $b): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución de Weibull cuyo parámetro de forma es `a` y el parámetro de escala es `b`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`a`  
El parámetro de forma de la distribución

`b`  
El parámetro de escala de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
