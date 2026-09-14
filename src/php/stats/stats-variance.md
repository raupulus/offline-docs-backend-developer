---
title: stats_variance
description: Devuelve la varianza
source_url: https://www.php.net/manual/es/function.stats-variance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-variance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87460
---

stats_variance

Devuelve la varianza

## Descripción

```php
stats_variance(array $a, [bool $sample]): float
```php

Devuelve la varianza de los valores en `a`.

## Parámetros

`a`  
El array de datos para el cual se calcula la varianza. Se debe tener en cuenta que todos los valores del array serán convertidos en `float`.

`sample`  
Indica si `a` representa una muestra de la población; por omisión es `false`.

## Valores devueltos

Devuelve la varianza en caso de éxito; `false` en caso de fallo.
