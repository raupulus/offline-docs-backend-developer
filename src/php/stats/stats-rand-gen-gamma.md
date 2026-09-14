---
title: stats_rand_gen_gamma
description: Genera una desviación aleatoria de la distribución gamma
source_url: https://www.php.net/manual/es/function.stats-rand-gen-gamma.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-rand-gen-gamma.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87210
---

stats_rand_gen_gamma

Genera una desviación aleatoria de la distribución gamma

## Descripción

```php
stats_rand_gen_gamma(float $a, float $r): float
```php

Genera una desviación aleatoria de la distribución gamma cuya densidad es (A\*\*R)/Gamma(R) \* X\*\*(R-1) \* Exp(-A\*X).

## Parámetros

`a`  
El parámetro de localización de la distribución gamma (`a` \> 0).

`r`  
El parámetro de forma de la distribución gamma (`r` \> 0).

## Valores devueltos

Una desviación aleatoria
