---
title: fann_get_learning_momentum
description: Devuelve el momento del aprendizaje
source_url: https://www.php.net/manual/es/function.fann-get-learning-momentum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-learning-momentum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21350
---

fann_get_learning_momentum

Devuelve el momento del aprendizaje

## Descripción

```php
fann_get_learning_momentum(resource $ann): float
```php

El momento del aprendizaje se puede emplear para acelerar un entrenamiento `FANN_TRAIN_INCREMENTAL`. Sin embargo, un momento muy alto no beneficiará al entrenamiento. Establecer el momento a 0 es lo mismo que no emplear el parmámetro del momento. El valor recomendado para el valor de este parámetro está entre 0.0 y 1.0.

El momento predeterminado es 0.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

El moemento del aprendizaje, o `false` en caso de error.

## Véase también

`fann_set_learning_momentum`, `fann_set_training_algorithm`
