---
title: stats_dens_f
description: La función de densidad de probabilidad de la distribución F
source_url: https://www.php.net/manual/es/function.stats-dens-f.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-f.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87020
---

stats_dens_f

La función de densidad de probabilidad de la distribución F

## Descripción

```php
stats_dens_f(float $x, float $dfr1, float $dfr2): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución F cuyos grados de libertad son `dfr1` y `dfr2`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`dfr1`  
El grado de libertad de la distribución

`dfr2`  
El grado de libertad de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
