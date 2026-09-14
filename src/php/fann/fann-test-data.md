---
title: fann_test_data
description: Prueba un conjunto de datos de entrenamiento y calcula el ECM de dichos
  datos
source_url: https://www.php.net/manual/es/function.fann-test-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-test-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 22250
---

fann_test_data

Prueba un conjunto de datos de entrenamiento y calcula el ECM de dichos datos

## Descripción

```php
fann_test_data(resource $ann, resource $data): float
```php

Prueba un conjunto de datos de entrenamiento y calcula el ECM de dichos datos.

Esta función actualiza el ECM y los valores de fallo de bit.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`data`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

El ECM actualizado, o `false` en caso de error.

## Véase también

`fann_train_on_data`, `fann_train_epoch`, `fann_get_bit_fail`, `fann_get_MSE`, `fann_set_training_algorithm`
