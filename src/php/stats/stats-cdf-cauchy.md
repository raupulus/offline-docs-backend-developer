---
title: stats_cdf_cauchy
description: Calcula un parámetro de la distribución de Cauchy en función de otros
  valores
source_url: https://www.php.net/manual/es/function.stats-cdf-cauchy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-cauchy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86810
---

stats_cdf_cauchy

Calcula un parámetro de la distribución de Cauchy en función de otros valores

## Descripción

```php
stats_cdf_cauchy(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución de Cauchy. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, x0, y gamma designan la función de distribución acumulativa, el valor de la variable aleatoria, el parámetro de localización y el parámetro de escala de la distribución de Cauchy, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | x0     | gamma  |
| 2       | x                | CDF    | x0     | gamma  |
| 3       | x0               | x      | CDF    | gamma  |
| 4       | gamma            | x      | CDF    | x0     |

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

Devuelve CDF, x, x0, o gamma, determinado por `which`.
