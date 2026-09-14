---
title: fann_set_learning_momentum
description: Establece el momento del aprendizaje
source_url: https://www.php.net/manual/es/function.fann-set-learning-momentum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-learning-momentum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22030
---

fann_set_learning_momentum

Establece el momento del aprendizaje

## Descripción

```php
fann_set_learning_momentum(resource $ann, float $learning_momentum): bool
```php

Establece el momento del aprendizaje.

Hay más información disponible en `fann_get_learning_momentum`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`learning_momentum`  
El momento del aprendizaje

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_learning_momentum`, `fann_set_training_algorithm`
