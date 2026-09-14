---
title: fann_set_activation_function_layer
description: Establece la función de activación para todas las neuronas de la capa
  proporcionada
source_url: https://www.php.net/manual/es/function.fann-set-activation-function-layer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-function-layer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 21790
---

fann_set_activation_function_layer

Establece la función de activación para todas las neuronas de la capa proporcionada

## Descripción

```php
fann_set_activation_function_layer(resource $ann, int $activation_function, int $layer): bool
```php

Establece la función de activación para todas las neuronas de la capa número `layer`, contanldo la capa de entrada como capa 0.

No es posible establecer funciones de activación para las neuronas de la capa de entrada.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_function`  
La constante de [funciones de activación](#constants.fann-activation-funcs).

`layer`  
El número de capa.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_function`, `fann_set_activation_function_hidden`, `fann_set_activation_function_output`, `fann_set_activation_steepness`
