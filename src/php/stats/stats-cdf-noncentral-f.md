---
title: stats_cdf_noncentral_f
description: Calcula un parámetro de la distribución F no central en función de los
  otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-noncentral-f.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-noncentral-f.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86900
---

stats_cdf_noncentral_f

Calcula un parámetro de la distribución F no central en función de los otros valores

## Descripción

```php
stats_cdf_noncentral_f(float $par1, float $par2, float $par3, float $par4, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución F no central. El tipo de la valor de retorno y los parámetros (`par1`, `par2`, `par3`, y `par4`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, nu1, nu2, y lambda designan la función de distribución acumulativa, el valor de la variable aleatoria, los grados de libertad y el parámetro de no centralidad de la distribución F no central, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` | `par4` |
|---------|------------------|--------|--------|--------|--------|
| 1       | CDF              | x      | nu1    | nu2    | lambda |
| 2       | x                | CDF    | nu1    | nu2    | lambda |
| 3       | nu1              | x      | CDF    | nu2    | lambda |
| 4       | nu2              | x      | CDF    | nu1    | lambda |
| 5       | lambda           | x      | CDF    | nu1    | nu2    |

Valor de retorno y parámetros

## Parámetros

`par1`  
El primer parámetro

`par2`  
El segundo parámetro

`par3`  
El tercer parámetro

`par4`  
El cuarto parámetro

`which`  
El flag para determinar qué debe ser calculado

## Valores devueltos

Devuelve CDF, x, nu1, nu2, o lambda, determinado por `which`.
