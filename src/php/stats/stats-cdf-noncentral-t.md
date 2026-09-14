---
title: stats_cdf_noncentral_t
description: Calcula un parámetro de la distribución t no central en función de los
  otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-noncentral-t.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-noncentral-t.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86910
---

stats_cdf_noncentral_t

Calcula un parámetro de la distribución t no central en función de los otros valores

## Descripción

```php
stats_cdf_noncentral_t(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución t no central. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La siguiente tabla lista el valor de retorno y los parámetros por `which`. CDF, x, nu, y mu designan la función de distribución acumulativa, el valor de la variable aleatoria, los grados de libertad y el parámetro de no centralidad de la distribución, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | nu     | mu     |
| 2       | x                | CDF    | nu     | mu     |
| 3       | nu               | x      | CDF    | mu     |
| 4       | mu               | x      | CDF    | nu     |

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

Devuelve CDF, x, nu, o mu, determinado por `which`.
