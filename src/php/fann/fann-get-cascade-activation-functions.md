---
title: fann_get_cascade_activation_functions
description: Devuelve las funciones de activación en cascada
source_url: https://www.php.net/manual/es/function.fann-get-cascade-activation-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-activation-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21150
---

fann_get_cascade_activation_functions

Devuelve las funciones de activación en cascada

## Descripción

```php
fann_get_cascade_activation_functions(resource $ann): array
```php

El array de funciones de activación en cascada es un array con las diferentes funciones de activación empleadas por las cadidatas.

Véase `fann_get_cascade_num_candidates` para una descripción de las neuronas candidatas generadas por este array.

Las funciones de activación predeterminadas son `FANN_SIGMOID`, `FANN_SIGMOID_SYMMETRIC`, `FANN_GAUSSIAN`, `FANN_GAUSSIAN_SYMMETRIC`, `FANN_ELLIOT` y `FANN_ELLIOT_SYMMETRIC`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Las funciones de activación en cascada, o `false` en caso de error.

## Véase también

`fann_get_cascade_activation_functions_count`, `fann_set_cascade_activation_functions`
