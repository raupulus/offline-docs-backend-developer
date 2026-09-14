---
title: stats_dens_chisquare
description: La función de densidad de probabilidad de la distribución chi-cuadrado
source_url: https://www.php.net/manual/es/function.stats-dens-chisquare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-dens-chisquare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87000
---

stats_dens_chisquare

La función de densidad de probabilidad de la distribución chi-cuadrado

## Descripción

```php
stats_dens_chisquare(float $x, float $dfr): float
```php

Devuelve la densidad de probabilidad en `x`, donde la variable aleatoria sigue la distribución chi-cuadrado con grados de libertad `dfr`.

## Parámetros

`x`  
El valor en el cual se calcula la densidad de probabilidad

`dfr`  
Los grados de libertad de la distribución

## Valores devueltos

La densidad de probabilidad en `x` o `false` en caso de error.
