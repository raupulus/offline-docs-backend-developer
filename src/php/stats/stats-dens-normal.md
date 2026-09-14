---
title: stats_dens_normal
description: La función de densidad de probabilidad de la distribución normal
source_url: https://www.php.net/manual/es/function.stats-dens-normal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-normal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87060
---

stats_dens_normal

La función de densidad de probabilidad de la distribución normal

## Descripción

```php
stats_dens_normal(float $x, float $ave, float $stdev): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución normal con media `ave` y desviación estándar `stdev`.

## Parámetros

`x`  
El valor en el que se calcula la densidad de probabilidad

`ave`  
La media de la distribución

`stdev`  
La desviación estándar de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
