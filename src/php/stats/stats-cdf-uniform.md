---
title: stats_cdf_uniform
description: Calcula un parámetro de la distribución uniforme en función de otros
  valores
source_url: https://www.php.net/manual/es/function.stats-cdf-uniform.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-uniform.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86950
---

stats_cdf_uniform

Calcula un parámetro de la distribución uniforme en función de otros valores

## Descripción

```php
stats_cdf_uniform(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución uniforme. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, a, y b designan la función de distribución acumulativa, el valor de la variable aleatoria, y los límites inferior y superior de la distribución uniforme, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | a      | b      |
| 2       | x                | CDF    | a      | b      |
| 3       | a                | x      | CDF    | b      |
| 4       | b                | x      | CDF    | a      |

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

Devuelve CDF, x, a, o b, determinado por `which`.
