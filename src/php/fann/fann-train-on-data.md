---
title: fann_train_on_data
description: Entrena un conjunto de datos completo por un período de tiempo
source_url: https://www.php.net/manual/es/function.fann-train-on-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-train-on-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22280
---

fann_train_on_data

Entrena un conjunto de datos completo por un período de tiempo

## Descripción

```php
fann_train_on_data(resource $ann, resource $data, int $max_epochs, int $epochs_between_reports, float $desired_error): bool
```php

Entrena un conjunto de datos completo por un período de tiempo.

Este entrenamiento emplea el algoritmo de entrenamiento elegido mediante `fann_set_training_algorithm` y los parámetros establecidos para estos algoritmos de entrenamiento.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`data`  
Un `resource` de datos de entrenamiento de red neuronal.

`max_epochs`  
El número máximo de épocas que debería continuar el entrenamiento.

`epochs_between_reports`  
El número de épocas entre llamadas a funciones de retrollamada. Un valor de cero significa que no se llamará a la función del usuario.

`desired_error`  
El `fann_get_MSE` o `fann_get_bit_fail` deseados, dependiendo de la función de parada elegida mediante `fann_set_train_stop_function`.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_train_on_file`, `fann_train_epoch`, `fann_get_bit_fail`, `fann_get_MSE`, `fann_set_train_stop_function`, `fann_set_training_algorithm`, `fann_set_callback`
