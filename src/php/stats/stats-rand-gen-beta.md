---
title: stats_rand_gen_beta
description: Genera una desviación aleatoria de la distribución beta
source_url: https://www.php.net/manual/es/function.stats-rand-gen-beta.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-rand-gen-beta.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87160
---

stats_rand_gen_beta

Genera una desviación aleatoria de la distribución beta

## Descripción

```php
stats_rand_gen_beta(float $a, float $b): float
```php

Devuelve una desviación aleatoria de la distribución beta con los parámetros A y B. La densidad de la beta es x^(a-1) \* (1-x)^(b-1) / B(a, b) para 0 \< x \<. Método R. C. H. Cheng.

## Parámetros

`a`  
El parámetro de forma de la distribución beta

`b`  
El parámetro de forma de la distribución beta

## Valores devueltos

Una desviación aleatoria
