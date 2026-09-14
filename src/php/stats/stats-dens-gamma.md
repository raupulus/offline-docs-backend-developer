---
title: stats_dens_gamma
description: La función de densidad de probabilidad de la distribución gamma
source_url: https://www.php.net/manual/es/function.stats-dens-gamma.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-gamma.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87030
---

stats_dens_gamma

La función de densidad de probabilidad de la distribución gamma

## Descripción

```php
stats_dens_gamma(float $x, float $shape, float $scale): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución gamma cuyo parámetro de forma es `shape` y el parámetro de escala es `scale`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`shape`  
El parámetro de forma de la distribución

`scale`  
El parámetro de escala de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
