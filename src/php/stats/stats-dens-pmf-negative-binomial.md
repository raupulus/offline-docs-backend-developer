---
title: stats_dens_pmf_negative_binomial
description: La función de masa de probabilidad de la distribución binomial negativa
source_url: https://www.php.net/manual/es/function.stats-dens-pmf-negative-binomial.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-pmf-negative-binomial.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87090
---

stats_dens_pmf_negative_binomial

La función de masa de probabilidad de la distribución binomial negativa

## Descripción

```php
stats_dens_pmf_negative_binomial(float $x, float $n, float $pi): float
```php

Devuelve la masa de probabilidad en `x`, donde la variable aleatoria sigue la distribución binomial negativa cuyo número de éxitos es `n` y la tasa de éxito es `pi`.

## Parámetros

`x`  
El valor en el cual se calcula la masa de probabilidad

`n`  
El número de éxitos de la distribución

`pi`  
La tasa de éxito de la distribución

## Valores devueltos

La masa de probabilidad en `x` o `false` en caso de error.
