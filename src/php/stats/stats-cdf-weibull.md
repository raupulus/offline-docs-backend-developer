---
title: stats_cdf_weibull
description: Calcula un parámetro de la distribución de Weibull en función de otros
  valores
source_url: https://www.php.net/manual/es/function.stats-cdf-weibull.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-weibull.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86960
---

stats_cdf_weibull

Calcula un parámetro de la distribución de Weibull en función de otros valores

## Descripción

```php
stats_cdf_weibull(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución de Weibull. El tipo de la valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La siguiente tabla lista el valor de retorno y los parámetros por `which`. CDF, x, k, y lambda designan la función de distribución acumulativa, el valor de la variable aleatoria, y los parámetros de forma y escala de la distribución de Weibull, respectivamente.

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
