---
title: fann_get_cascade_candidate_stagnation_epochs
description: Devuelve el número de épocas de estancamiento de candidatas en cascada
source_url: https://www.php.net/manual/es/function.fann-get-cascade-candidate-stagnation-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-candidate-stagnation-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21200
---

fann_get_cascade_candidate_stagnation_epochs

Devuelve el número de épocas de estancamiento de candidatas en cascada

## Descripción

```php
fann_get_cascade_candidate_stagnation_epochs(resource $ann): int
```php

El número de épocas de estancamiento de candidatas en cascada determina el número de entrenamiento de épocas permitido para continuar sin cambiar el ECM por una fracción de `fann_get_cascade_candidate_change_fraction`.

Véase más información sobre este parámetro en `fann_get_cascade_candidate_change_fraction`.

El número de épocas de estancamiento de candidatas en cascada predeterminado es 12.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número de épocas de estancamiento de candidatas en cascada, o `false` en caso de error.

## Véase también

`fann_set_cascade_candidate_stagnation_epochs`, `fann_get_cascade_candidate_change_fraction`
