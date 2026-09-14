---
title: fann_scale_train_data
description: Escala la entradas y salidas de los datos de entrenamiento al rango especificado
source_url: https://www.php.net/manual/es/function.fann-scale-train-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-scale-train-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21760
---

fann_scale_train_data

Escala la entradas y salidas de los datos de entrenamiento al rango especificado

## Descripción

```php
fann_scale_train_data(resource $train_data, float $new_min, float $new_max): bool
```php

Escala la entradas y salidas de los datos de entrenamiento al rango especificado.

## Parámetros

`train_data`  
Un `resource` de datos de entrenamiento de red neuronal.

`new_min`  
El nuevo mínimo después de escalar las entradas y salidas de los datos de entrenamiento.

`new_max`  
El nuevo máximo después de escalar las entradas y salidas de los datos de entrenamiento.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_scale_output_train_data`, `fann_scale_input_train_data`
