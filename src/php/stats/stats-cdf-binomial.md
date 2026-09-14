---
title: stats_cdf_binomial
description: Calcula un argumento de la distribución binomial en función de los otros
  valores
source_url: https://www.php.net/manual/es/function.stats-cdf-binomial.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-binomial.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86800
---

stats_cdf_binomial

Calcula un argumento de la distribución binomial en función de los otros valores

## Descripción

```php
stats_cdf_binomial(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los argumentos, de la distribución binomial. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La siguiente tabla lista el valor de retorno y los parámetros por `which`. CDF, x, n, y p designan la función de distribución acumulativa, el número de éxitos, el número de intentos, y la tasa de éxito para cada intento, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | n      | p      |
| 2       | x                | CDF    | n      | p      |
| 3       | n                | x      | CDF    | p      |
| 4       | p                | x      | CDF    | n      |

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

Devuelve CDF, x, n, o p, determinado por `which`.
