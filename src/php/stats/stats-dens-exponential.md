---
title: stats_dens_exponential
description: La función de densidad de probabilidad de la distribución exponencial
source_url: https://www.php.net/manual/es/function.stats-dens-exponential.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-exponential.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87010
---

stats_dens_exponential

La función de densidad de probabilidad de la distribución exponencial

## Descripción

```php
stats_dens_exponential(float $x, float $scale): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución exponencial cuya escala es `scale`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`scale`  
La escala de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
