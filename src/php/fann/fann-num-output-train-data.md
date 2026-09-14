---
title: fann_num_output_train_data
description: Devuelve el número de salidas de cada patrón de entrenamiento de los
  datos de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-num-output-train-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-num-output-train-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21620
---

fann_num_output_train_data

Devuelve el número de salidas de cada patrón de entrenamiento de los datos de entrenamiento

## Descripción

```php
fann_num_output_train_data(resource $data): int
```php

Devuelve el número de salidas de cada patrón de entrenamiento del `resource` de datos de entrenamiento.

## Parámetros

`data`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

El número de salidas, o `false` en caso de error.

## Véase también

`fann_length_train_data`, `fann_num_input_train_data`
