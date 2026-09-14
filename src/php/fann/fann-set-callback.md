---
title: fann_set_callback
description: Establece la función de retrollamada a emplear durante el entrenamiento
source_url: https://www.php.net/manual/es/function.fann-set-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 83b687a15
order: 21870
---

fann_set_callback

Establece la función de retrollamada a emplear durante el entrenamiento

## Descripción

```php
fann_set_callback(resource $ann, callable $callback): bool
```php

Establece la función de retrollamada a emplear durante el entrenamiento. Esto significa que es llamada desde `fann_train_on_data` o `fann_train_on_file`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`callback`  
La función de retrollamada proporcionada toma los siguientes parámetros: `ann` - El `resource` de red neuronal, `train` - El `resource` de datos de entrenamiento o `null` si se llamada desde `fann_train_on_file`, `max_epochs` - El número máximo de épocas que debería continuar el entrenamiento, `epochs_between_reports` - El número de épocas entre llamadas a esta función, `desired_error` - El `fann_get_MSE` deseado o `fann_get_bit_fail`, dependiendo de la función de parada elegida mediante `fann_set_train_stop_function`, `epochs` - La época actual

La retrollamada debería devolver `true`. Si devuelve `false`, el entrenamiento finalizará.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_train_on_data`, `fann_train_on_file`
