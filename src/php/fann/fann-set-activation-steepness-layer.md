---
title: fann_set_activation_steepness_layer
description: Establece la pendiente de activación para todas las neuronas del número
  de capa proporcionada
source_url: https://www.php.net/manual/es/function.fann-set-activation-steepness-layer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-steepness-layer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21830
---

fann_set_activation_steepness_layer

Establece la pendiente de activación para todas las neuronas del número de capa proporcionada

## Descripción

```php
fann_set_activation_steepness_layer(resource $ann, float $activation_steepness, int $layer): bool
```php

Establece la pendiente de activación para todas las neuronas de la capa número `layer`, contando la capa de entrada como capa 0.

No es posible establecer una pendiente de activación en la capa de entrada.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_steepness`  
La pendiente de activación.

`layer`  
El número de capa.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_steepness`, `fann_set_activation_steepness_hidden`, `fann_set_activation_steepness_output`, `fann_get_activation_steepness`, `fann_set_activation_function`
