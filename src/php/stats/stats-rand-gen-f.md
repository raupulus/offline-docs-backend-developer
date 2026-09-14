---
title: stats_rand_gen_f
description: Genera una desviación aleatoria de la distribución F
source_url: https://www.php.net/manual/es/function.stats-rand-gen-f.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-rand-gen-f.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87190
---

stats_rand_gen_f

Genera una desviación aleatoria de la distribución F

## Descripción

```php
stats_rand_gen_f(float $dfn, float $dfd): float
```php

Genera una desviación aleatoria de la distribución F (ratio de varianza) con "dfn" grados de libertad en el numerador y "dfd" grados de libertad en el denominador. Método: genera directamente el ratio de variables chi-cuadrado.

## Parámetros

`dfn`  
El grado de libertad en el numerador

`dfd`  
El grado de libertad en el denominador

## Valores devueltos

Una desviación aleatoria
