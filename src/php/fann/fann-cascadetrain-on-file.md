---
title: fann_cascadetrain_on_file
description: Entrena una red neuronal sobre un conjunto completo de datos durante
  un período de tiempo utilizando el algoritmo de entrenamiento Cascade2
source_url: https://www.php.net/manual/es/function.fann-cascadetrain-on-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-cascadetrain-on-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 20910
---

fann_cascadetrain_on_file

Entrena una red neuronal sobre un conjunto completo de datos durante un período de tiempo utilizando el algoritmo de entrenamiento Cascade2

## Descripción

```php
fann_cascadetrain_on_file(resource $ann, string $filename, int $max_neurons, int $neurons_between_reports, float $desired_error): bool
```php

Realiza la misma operación que `fann_cascadetrain_on_data`, pero lee los datos de entrenamiento directamente desde un fichero.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`filename`  
Un fichero que contiene los datos para el entrenamiento.

`max_neurons`  
El número máximo de neuronas a añadir a la red neuronal.

`neurons_between_reports`  
El número de neuronas entre la impresión de un informe de estado. Un valor de cero indica que no debe mostrarse ningún informe.

`desired_error`  
La `fann_get_MSE` o `fann_get_bit_fail` deseada, según la función de parada seleccionada por `fann_set_train_stop_function`.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_train_on_data`, `fann_cascadetrain_on_data`
