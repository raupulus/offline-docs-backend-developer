---
title: stats_stat_correlation
description: Devuelve el coeficiente de correlación de Pearson de dos conjuntos de
  datos
source_url: https://www.php.net/manual/es/function.stats-stat-correlation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-stat-correlation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87390
---

stats_stat_correlation

Devuelve el coeficiente de correlación de Pearson de dos conjuntos de datos

## Descripción

```php
stats_stat_correlation(array $arr1, array $arr2): float
```php

Devuelve el coeficiente de correlación de Pearson entre `arr1` y `arr2`.

## Parámetros

`arr1`  
El primer array

`arr2`  
El segundo array

## Valores devueltos

Devuelve el coeficiente de correlación de Pearson entre `arr1` y `arr2`, o `false` en caso de fallo.
