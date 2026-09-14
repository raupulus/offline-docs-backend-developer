---
title: stats_cdf_poisson
description: Calcula un parámetro de la distribución de Poisson en función de los
  otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-poisson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-poisson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86930
---

stats_cdf_poisson

Calcula un parámetro de la distribución de Poisson en función de los otros valores

## Descripción

```php
stats_cdf_poisson(float $par1, float $par2, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución de Poisson. El tipo del valor de retorno y los parámetros (`par1` y `par2`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, y lambda designan la función de distribución acumulativa, el valor de la variable aleatoria, y el parámetro de la distribución de Poisson, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` |
|---------|------------------|--------|--------|
| 1       | CDF              | x      | lambda |
| 2       | x                | CDF    | lambda |
| 3       | lambda           | x      | CDF    |

Valor de retorno y parámetros

## Parámetros

`par1`  
El primer parámetro

`par2`  
El segundo parámetro

`which`  
El flag para determinar qué debe ser calculado

## Valores devueltos

Devuelve CDF, x, o lambda, determinado por `which`.
