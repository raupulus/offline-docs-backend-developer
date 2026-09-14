---
title: stats_dens_pmf_poisson
description: La función de masa de probabilidad de la distribución de Poisson
source_url: https://www.php.net/manual/es/function.stats-dens-pmf-poisson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-pmf-poisson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87100
---

stats_dens_pmf_poisson

La función de masa de probabilidad de la distribución de Poisson

## Descripción

```php
stats_dens_pmf_poisson(float $x, float $lb): float
```php

Devuelve la masa de probabilidad en `x`, donde la variable aleatoria sigue la distribución de Poisson cuyo parámetro es `lb`.

## Parámetros

`x`  
El valor en el cual se calcula la masa de probabilidad

`lb`  
El parámetro de la distribución de Poisson

## Valores devueltos

La masa de probabilidad en `x` o `false` en caso de error.
