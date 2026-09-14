---
title: stats_dens_uniform
description: La función de densidad de probabilidad de la distribución uniforme
source_url: https://www.php.net/manual/es/function.stats-dens-uniform.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-uniform.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87120
---

stats_dens_uniform

La función de densidad de probabilidad de la distribución uniforme

## Descripción

```php
stats_dens_uniform(float $x, float $a, float $b): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución uniforme cuyo límite inferior es `a` y el límite superior es `b`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`a`  
El límite inferior de la distribución

`b`  
El límite superior de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
