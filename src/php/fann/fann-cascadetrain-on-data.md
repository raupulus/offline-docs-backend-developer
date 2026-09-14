---
title: fann_cascadetrain_on_data
description: Entrena un conjunto de datos completo, por un período de tiempo utilizando
  el algoritmo de entrenamiento Cascade2
source_url: https://www.php.net/manual/es/function.fann-cascadetrain-on-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-cascadetrain-on-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 20900
---

fann_cascadetrain_on_data

Entrena un conjunto de datos completo, por un período de tiempo utilizando el algoritmo de entrenamiento Cascade2

## Descripción

```php
fann_cascadetrain_on_data(resource $ann, resource $data, int $max_neurons, int $neurons_between_reports, float $desired_error): bool
```php

La fracción de cambio de salida en cascada es un número entre 0 y 1 que determina lo grande que debería ser el cambio del valor de una fracción de `fann_get_MSE` en `fann_get_cascade_output_stagnation_epochs` durante el entrenamiento de las conexiones de salida, para que el entrenamiento no se estanque. Si el entrenamiento se estanca, el entrenamiento de las conexiones de salida finalizará y se prepararán nuevas candidatas.

Este entrenamiento emplea los parámetros establecidos en las funciones fann_set_cascade\_..., aunque también emplea otro algoritmo de entrenamiento debido a su algoritmo de entrenamiento interno. Este algoritmo se puede establecer a `FANN_TRAIN_RPROP` o `FANN_TRAIN_QUICKPROP` mediante `fann_set_training_algorithm`, y los parámetros establecidos para estos algoritmos de entrenamiento también afectarán al entrenamiento en cascada.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`data`  
Un `resource` de datos de entrenamiento de red neuronal.

`max_neurons`  
El número máximo de neuronas a añadir a la red neuronal.

`neurons_between_reports`  
El número de neuronas entre impresiones de informes de estado. Un valor de cero significa que no deberían imprimirse informes.

`desired_error`  
El `fann_get_MSE` o `fann_get_bit_fail` deseados, dependiendo de la función de parada elegida mediante `fann_set_train_stop_function`.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_train_on_data`, `fann_cascadetrain_on_file`
