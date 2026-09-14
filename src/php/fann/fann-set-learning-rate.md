---
title: fann_set_learning_rate
description: Establece el índice de aprendizaje
source_url: https://www.php.net/manual/es/function.fann-set-learning-rate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-learning-rate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22040
---

fann_set_learning_rate

Establece el índice de aprendizaje

## Descripción

```php
fann_set_learning_rate(resource $ann, float $learning_rate): bool
```php

Establece el índice de aprendizaje.

Hay más información en `fann_get_learning_rate`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`learning_rate`  
El índice de aprendizaje.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_learning_rate`, `fann_set_training_algorithm`
