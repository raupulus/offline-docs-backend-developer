---
title: stats_rand_gen_noncentral_f
description: Genera una desviación aleatoria de la distribución F no central
source_url: https://www.php.net/manual/es/function.stats-rand-gen-noncentral-f.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-rand-gen-noncentral-f.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87280
---

stats_rand_gen_noncentral_f

Genera una desviación aleatoria de la distribución F no central

## Descripción

```php
stats_rand_gen_noncentral_f(float $dfn, float $dfd, float $xnonc): float
```php

Devuelve una desviación aleatoria de la distribución F no central con los grados de libertad, `dfn` (numerador) y `dfd` (denominador), y el parámetro de no centralidad, `xnonc`.

## Parámetros

`dfn`  
Los grados de libertad del numerador

`dfd`  
Los grados de libertad del denominador

`xnonc`  
El parámetro de no centralidad

## Valores devueltos

Una desviación aleatoria
