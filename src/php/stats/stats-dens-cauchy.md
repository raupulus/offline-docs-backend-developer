---
title: stats_dens_cauchy
description: La función de densidad de probabilidad de la distribución de Cauchy
source_url: https://www.php.net/manual/es/function.stats-dens-cauchy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-cauchy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86990
---

stats_dens_cauchy

La función de densidad de probabilidad de la distribución de Cauchy

## Descripción

```php
stats_dens_cauchy(float $x, float $ave, float $stdev): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución de Cauchy cuyos parámetros de ubicación y escala son `ave` y `stdev`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`ave`  
El parámetro de ubicación de la distribución

`stdev`  
El parámetro de escala de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
