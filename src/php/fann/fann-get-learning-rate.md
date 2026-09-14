---
title: fann_get_learning_rate
description: Devuelve el índice de aprendizaje
source_url: https://www.php.net/manual/es/function.fann-get-learning-rate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-learning-rate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21360
---

fann_get_learning_rate

Devuelve el índice de aprendizaje

## Descripción

```php
fann_get_learning_rate(resource $ann): float
```php

El índice de aprendizaje se emplea para determinar la agresividad de un entrenamiento para algunos de los algoritmo de entrenamiento (`FANN_TRAIN_INCREMENTAL`, `FANN_TRAIN_BATCH` y `FANN_TRAIN_QUICKPROP`). Observe, sin embargo, que no se emplea en `FANN_TRAIN_RPROP`.

El índice de aprendizaje predeterminado es 0.7.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El índice de aprendizaje, o `false` en caso de error.

## Véase también

`fann_set_learning_rate`, `fann_set_training_algorithm`
