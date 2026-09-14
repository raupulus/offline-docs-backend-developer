---
title: stats_cdf_f
description: Calcula un parámetro de la distribución F en función de otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-f.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-f.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86840
---

stats_cdf_f

Calcula un parámetro de la distribución F en función de otros valores

## Descripción

```php
stats_cdf_f(float $par1, float $par2, float $par3, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución F. El tipo de la valor de retorno y los parámetros (`par1`, `par2`, y `par3`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, d1, y d2 designan la función de distribución acumulativa, el valor de la variable aleatoria, y los grados de libertad de la distribución F, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` | `par3` |
|---------|------------------|--------|--------|--------|
| 1       | CDF              | x      | d1     | d2     |
| 2       | x                | CDF    | d1     | d2     |
| 3       | d1               | x      | CDF    | d2     |
| 4       | d2               | x      | CDF    | d1     |

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

Devuelve CDF, x, d1, o d2, determinado por `which`.
