---
title: stats_cdf_noncentral_chisquare
description: Calcula un argumento de la distribución del chi-cuadrado no central en
  función de otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-noncentral-chisquare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-noncentral-chisquare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_reviewed: false
translation_revision: c6542ce86
order: 86890
---

stats_cdf_noncentral_chisquare

Calcula un argumento de la distribución del chi-cuadrado no central en función de otros valores

## Descripción

```php
stats_cdf_noncentral_chisquare(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución binomial. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, k, y lambda designan la función de distribución acumulativa, el valor de la variable aleatoria, el grado de libertad y el argumento de no centralidad de la distribución del chi-cuadrado no central, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | k      | lambda |
| 2       | x                | CDF    | k      | lambda |
| 3       | k                | x      | CDF    | lambda |
| 4       | lambda           | x      | CDF    | k      |

Valor de retorno y parámetros

## Parámetros

`par1`  
El primer parámetro

`par2`  
El segundo parámetro

`par3`  
El tercer parámetro

`which`  
El flag para determinar qué debe ser calculado

## Valores devueltos

Devuelve CDF, x, k, o lambda, determinado por `which`.
