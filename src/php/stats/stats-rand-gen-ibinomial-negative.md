---
title: stats_rand_gen_ibinomial_negative
description: Genera una desviación aleatoria de la distribución binomial negativa
source_url: https://www.php.net/manual/es/function.stats-rand-gen-ibinomial-negative.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-rand-gen-ibinomial-negative.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87220
---

stats_rand_gen_ibinomial_negative

Genera una desviación aleatoria de la distribución binomial negativa

## Descripción

```php
stats_rand_gen_ibinomial_negative(int $n, float $p): int
```php

Devuelve una desviación aleatoria de la distribución binomial negativa donde el número de éxitos es `n` y la tasa de éxito es `p`.

## Parámetros

`n`  
El número de éxitos.

`p`  
La tasa de éxito.

## Valores devueltos

Una desviación aleatoria, que es el número de fracasos.
