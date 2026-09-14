---
title: fann_get_cascade_num_candidates
description: Devuelve el número de candidatas empleadas durante un entrenamiento
source_url: https://www.php.net/manual/es/function.fann-get-cascade-num-candidates.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-num-candidates.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21260
---

fann_get_cascade_num_candidates

Devuelve el número de candidatas empleadas durante un entrenamiento

## Descripción

```php
fann_get_cascade_num_candidates(resource $ann): int
```php

El número de candidatas empleadas durante el entrenamiento (calculado multiplicando `fann_get_cascade_activation_functions_count`, `fann_get_cascade_activation_steepnesses_count` y `fann_get_cascade_num_candidate_groups`).

Las candidatas reales están definidos por los array `fann_get_cascade_activation_functions` y `fann_get_cascade_activation_steepnesses`. Estos array definen las funciones de activación y las pendientes de activación empleadas por las neuronas candidatas. Si hay 2 funciones de activación en el array de funciones de activación y 3 pendientes en el array de pendientes, habrá 2x3=6 candidatas diferentes que serán entrenados. Estas 6 candidatas diferentes se puedn copiar a varios grupos de candidatas, donde la única diferencia entre estos grupos es el peso inicial. Si el número de grupos se establece a 2, el número de neuronas candidatas será 2x3x2=12. El número de grupos de candidatas está definido por `fann_set_cascade_num_candidate_groups`.

El número de candidatas predeterminado es 6x4x2 = 48

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número de candidatas emleadas durante un entrenamiento, o `false` en caso de error.

## Véase también

`fann_get_cascade_activation_functions`, `fann_get_cascade_activation_functions_count`, `fann_get_cascade_activation_steepnesses`, `fann_get_cascade_activation_steepnesses_count`, `fann_get_cascade_num_candidate_groups`
