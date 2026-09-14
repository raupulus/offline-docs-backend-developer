---
title: stats_standard_deviation
description: Devuelve la desviación estándar
source_url: https://www.php.net/manual/es/function.stats-standard-deviation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stats/functions/stats-standard-deviation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stats
translation_status: ready
translation_revision: c6542ce86
order: 87370
---

stats_standard_deviation

Devuelve la desviación estándar

## Descripción

```php
stats_standard_deviation(array $a, [bool $sample]): float
```php

Devuelve la desviación estándar de los valores en `a`.

## Parámetros

`a`  
El array de datos para el cual se calcula la desviación estándar. Es de notar que todos los valores del array serán convertidos en `float`.

`sample`  
Indica si `a` representa una muestra de la población; por omisión es `false`.

## Valores devueltos

Devuelve la desviación estándar en caso de éxito; `false` en caso de fallo.

## Errores/Excepciones

Lanza una `E_WARNING` cuando hay menos de 2 valores en `a`.
