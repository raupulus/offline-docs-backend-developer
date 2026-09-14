---
title: stats_cdf_beta
description: Calcula un parámetro de la distribución beta en función de otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-beta.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-beta.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86790
---

stats_cdf_beta

Calcula un parámetro de la distribución beta en función de otros valores

## Descripción

```php
stats_cdf_beta(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución beta. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La siguiente tabla lista el valor de retorno y los parámetros por `which`. CDF, x, alpha, y beta designan la función de distribución acumulativa, el valor de la variable aleatoria, y los parámetros de forma de la distribución beta, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | alpha  | beta   |
| 2       | x                | CDF    | alpha  | beta   |
| 3       | alpha            | x      | CDF    | beta   |
| 4       | beta             | x      | CDF    | alpha  |

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

Devuelve CDF, x, alpha, o beta, determinado por `which`.
