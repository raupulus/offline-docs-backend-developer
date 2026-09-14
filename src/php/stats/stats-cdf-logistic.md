---
title: stats_cdf_logistic
description: Calcula un parámetro de la distribución logística en función de otros
  valores
source_url: https://www.php.net/manual/es/function.stats-cdf-logistic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-logistic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86870
---

stats_cdf_logistic

Calcula un parámetro de la distribución logística en función de otros valores

## Descripción

```php
stats_cdf_logistic(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución logística. El tipo del valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La siguiente tabla lista el valor de retorno y los parámetros por `which`. CDF, x, mu, y s designan la función de distribución acumulativa, el valor de la variable aleatoria, y los parámetros de localización y escala de la distribución logística, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | mu     | s      |
| 2       | x                | CDF    | mu     | s      |
| 3       | mu               | x      | CDF    | s      |
| 4       | s                | x      | CDF    | mu     |

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

Devuelve CDF, x, mu, o s, determinado por `which`.
