---
title: fann_set_activation_steepness_hidden
description: Establece la pendiente de la activación para todas las neuronas de todas
  las capas ocultas
source_url: https://www.php.net/manual/es/function.fann-set-activation-steepness-hidden.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-steepness-hidden.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21820
---

fann_set_activation_steepness_hidden

Establece la pendiente de la activación para todas las neuronas de todas las capas ocultas

## Descripción

```php
fann_set_activation_steepness_hidden(resource $ann, float $activation_steepness): bool
```php

Establece la pendiente de la activación para todas las neuronas de todas las capas ocultas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_steepness`  
La pendiente de activación.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_steepness`, `fann_set_activation_steepness_layer`, `fann_set_activation_steepness_output`, `fann_get_activation_steepness`, `fann_set_activation_function`
