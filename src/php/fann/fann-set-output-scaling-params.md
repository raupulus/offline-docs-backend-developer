---
title: fann_set_output_scaling_params
description: Calcular los parámetros de escala de salida para un uso futuro basados
  en datos de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-set-output-scaling-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-output-scaling-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22050
---

fann_set_output_scaling_params

Calcular los parámetros de escala de salida para un uso futuro basados en datos de entrenamiento

## Descripción

```php
fann_set_output_scaling_params(resource $ann, resource $train_data, float $new_output_min, float $new_output_max): bool
```php

Calcular los parámetros de escala de salida para un uso futuro basados en datos de entrenamiento.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`train_data`  
Un `resource` de datos de entrenamiento de red neuronal.

`new_output_min`  
El límite inferior deseado de los datos de salida después de escalar (no seguido estrictamente)

`new_output_max`  
El límite superior deseado de los datos de salida después de escalar (no seguido estrictamente)

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_input_scaling_params`
