---
title: stats_cdf_normal
description: Calcule un parámetro de la distribución normal en función de los otros
  valores
source_url: https://www.php.net/manual/es/function.stats-cdf-normal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-normal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86920
---

stats_cdf_normal

Calcule un parámetro de la distribución normal en función de los otros valores

## Descripción

```php
stats_cdf_normal(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución normal. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, mu, y sigma designan la función de distribución acumulativa, el valor de la variable aleatoria, la media y la desviación estándar de la distribución normal, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | mu     | sigma  |
| 2       | x                | CDF    | mu     | sigma  |
| 3       | mu               | x      | CDF    | sigma  |
| 4       | sigma            | x      | CDF    | mu     |

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

Devuelve CDF, x, mu, o sigma, determinado por `which`.
