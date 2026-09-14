---
title: fann_set_training_algorithm
description: Establece el algoritmo de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-set-training-algorithm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-training-algorithm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22200
---

fann_set_training_algorithm

Establece el algoritmo de entrenamiento

## Descripción

```php
fann_set_training_algorithm(resource $ann, int $training_algorithm): bool
```php

Establece el algoritmo de entrenamiento.

Hay más información disponible en `fann_get_training_algorithm`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`training_algorithm`  
La constante de [Algoritno de entrenamiento](#constants.fann-train).

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_training_algorithm`
