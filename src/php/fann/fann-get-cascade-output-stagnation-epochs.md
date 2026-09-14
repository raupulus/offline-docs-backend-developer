---
title: fann_get_cascade_output_stagnation_epochs
description: Devuelve el número de épocas de estancamiento de salida en cascada
source_url: https://www.php.net/manual/es/function.fann-get-cascade-output-stagnation-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-output-stagnation-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21280
---

fann_get_cascade_output_stagnation_epochs

Devuelve el número de épocas de estancamiento de salida en cascada

## Descripción

```php
fann_get_cascade_output_stagnation_epochs(resource $ann): int
```php

El número de épocas de estacamiento de salida en cascada determina el número de épocas que se le permite al entrenamiento continuar sin cambiar el ECM por una fracción de `fann_get_cascade_output_change_fraction`.

Véase más información sobre este parámetro en `fann_get_cascade_output_change_fraction`.

El número predeterminado de épocas de estancamiento de salida en cascada es 12.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número de épocas de estancamiento de salida en cascada, o `false` en caso de error.

## Véase también

`fann_set_cascade_output_stagnation_epochs`, `fann_get_cascade_output_change_fraction`
