---
title: stats_dens_beta
description: La función de densidad de probabilidad de la distribución beta
source_url: https://www.php.net/manual/es/function.stats-dens-beta.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-beta.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 86980
---

stats_dens_beta

La función de densidad de probabilidad de la distribución beta

## Descripción

```php
stats_dens_beta(float $x, float $a, float $b): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución beta cuyos parámetros de forma son `a` y `b`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`a`  
El parámetro de forma de la distribución

`b`  
El parámetro de forma de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
