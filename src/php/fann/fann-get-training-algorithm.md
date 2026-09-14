---
title: fann_get_training_algorithm
description: Devuelve el algoritmo de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-get-training-algorithm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-training-algorithm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21570
---

fann_get_training_algorithm

Devuelve el algoritmo de entrenamiento

## Descripción

```php
fann_get_training_algorithm(resource $ann): int
```php

Devuelve el algoritmo de entrenamiento. Este algoritmo lo utilizan `fann_train_on_data` y funciones asociadas.

Observe que este algoritmo también se emplea durante `fann_cascadetrain_on_data`, aunque solamente están permitidos `FANN_TRAIN_RPROP` y `FANN_TRAIN_QUICKPROP` durante un entrenamiento en cascada.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

La constante de [Algoritmo de entrenamiento](#constants.fann-train), o `false` en caso de error.

## Véase también

`fann_set_training_algorithm`
