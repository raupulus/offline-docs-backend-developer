---
title: fann_get_activation_function
description: Devuelve la función de activación
source_url: https://www.php.net/manual/es/function.fann-get-activation-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-activation-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 21090
---

fann_get_activation_function

Devuelve la función de activación

## Descripción

```php
fann_get_activation_function(resource $ann, int $layer, int $neuron): int
```php

Obtiene la función de activación para la neurona número the `neuron` en la capa número `layer`, contando la capa de entrada como capa 0.

No es posible obtener funciones de activación para neuronas de la capa de entrada.

El valor devuelto es una de las constantes de [funciones de activación](#constants.fann-activation-funcs).

## Parámetros

`ann`  
Un `resource` de red neuronal.

`layer`  
El número de capa.

`neuron`  
El número de neurona.

## Valores devueltos

Una constante de [funciones de activación](#constants.fann-activation-funcs) o -1 si la neurona no está definida en la red neuronal, o `false` en caso de error.

## Véase también

`fann_set_activation_function_layer`, `fann_set_activation_function_hidden`, `fann_set_activation_function_output`, `fann_set_activation_steepness`, `fann_set_activation_function`
