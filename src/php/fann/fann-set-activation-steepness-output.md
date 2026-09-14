---
title: fann_set_activation_steepness_output
description: Establece la pendiente de activación de la capa de salida
source_url: https://www.php.net/manual/es/function.fann-set-activation-steepness-output.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-steepness-output.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21840
---

fann_set_activation_steepness_output

Establece la pendiente de activación de la capa de salida

## Descripción

```php
fann_set_activation_steepness_output(resource $ann, float $activation_steepness): bool
```php

Establece la pendiente de activación de la capa de salida.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_steepness`  
La pendiente de activación.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_steepness`, `fann_set_activation_steepness_layer`, `fann_set_activation_steepness_hidden`, `fann_get_activation_steepness`, `fann_set_activation_function`
