---
title: fann_set_activation_function
description: Establece la función de activación para la neurona y capa proporcionadas
source_url: https://www.php.net/manual/es/function.fann-set-activation-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21810
---

fann_set_activation_function

Establece la función de activación para la neurona y capa proporcionadas

## Descripción

```php
fann_set_activation_function(resource $ann, int $activation_function, int $layer, int $neuron): bool
```php

Establece la función de activación para la neurona número `neuron` en la capa número `layer`, contando al capa de entrada como capa 0.

No es posible establecer funciones de activación para las neuronas de la capa de entrada.

Al elegir una función de activación, es importante observar que las funciones de activación tienen un rango diferente. `FANN_SIGMOID` está, p.ej., en el rango 0 - 1, mientras que `FANN_SIGMOID_SYMMETRIC` está en el rango -1 - 1, y `FANN_LINEAR` no tiene límites.

The supplied activation_function value must be one of the [activation functions](#constants.fann-activation-funcs) constants.

El valor devuelto es una de las constantes de [funciones de activación](#constants.fann-train).

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_function`  
La constante de [funciones de activación](#constants.fann-activation-funcs).

`layer`  
El número de capa.

`neuron`  
El número de neurona.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_function_layer`, `fann_set_activation_function_hidden`, `fann_set_activation_function_output`, `fann_set_activation_steepness`, `fann_get_activation_function`
