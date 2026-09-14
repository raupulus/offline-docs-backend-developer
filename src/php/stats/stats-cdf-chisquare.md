---
title: stats_cdf_chisquare
description: Calcula un parámetro de la distribución del chi-cuadrado en función de
  los otros valores
source_url: https://www.php.net/manual/es/function.stats-cdf-chisquare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-cdf-chisquare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86820
---

stats_cdf_chisquare

Calcula un parámetro de la distribución del chi-cuadrado en función de los otros valores

## Descripción

```php
stats_cdf_chisquare(float $par1, float $par2, int $which): float
```php

Devuelve la función de distribución acumulativa, su inversa, o uno de los parámetros, de la distribución del chi-cuadrado. El tipo del valor de retorno y los parámetros (`par1` y `par2`) son determinados por `which`.

La tabla siguiente lista el valor de retorno y los parámetros por `which`. CDF, x, y k designan la función de distribución acumulativa, el valor de la variable aleatoria, y el grado de libertad de la distribución del chi-cuadrado, respectivamente.

| `which` | Valor de retorno | `par1` | `par2` |
|---------|------------------|--------|--------|
| 1       | CDF              | x      | k      |
| 2       | x                | CDF    | k      |
| 3       | k                | x      | CDF    |

Valor de retorno y parámetros

## Parámetros

`par1`  
El primer parámetro

`par2`  
El segundo parámetro

`which`  
El flag para determinar qué debe ser calculado

## Valores devueltos

Devuelve CDF, x, o k, determinado por `which`.
