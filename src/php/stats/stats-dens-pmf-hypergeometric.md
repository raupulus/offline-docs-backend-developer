---
title: stats_dens_pmf_hypergeometric
description: La función de masa de probabilidad de la distribución hipergeométrica
source_url: https://www.php.net/manual/es/function.stats-dens-pmf-hypergeometric.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-pmf-hypergeometric.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87080
---

stats_dens_pmf_hypergeometric

La función de masa de probabilidad de la distribución hipergeométrica

## Descripción

```php
stats_dens_pmf_hypergeometric(float $n1, float $n2, float $N1, float $N2): float
```php

Devuelve la masa de probabilidad en `n1`, donde la variable aleatoria sigue la distribución hipergeométrica cuyo número de fallos es `n2`, el número de muestras de éxito es `N1`, y el número de muestras de fallos es `N2`.

## Parámetros

`n1`  
El número de éxitos, a partir del cual se calcula la masa de probabilidad

`n2`  
El número de fallos de la distribución

`N1`  
El número de muestras de éxito de la distribución

`N2`  
El número de muestras de fallos de la distribución

## Valores devueltos

La masa de probabilidad en `n1` o `false` en caso de error.
