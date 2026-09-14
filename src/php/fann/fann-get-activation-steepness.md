---
title: fann_get_activation_steepness
description: Devuelve la pendiente de activación para el número de neurona y de capa
  proporcionados
source_url: https://www.php.net/manual/es/function.fann-get-activation-steepness.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-activation-steepness.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 9ee27f088
order: 21100
---

fann_get_activation_steepness

Devuelve la pendiente de activación para el número de neurona y de capa proporcionados

## Descripción

```php
fann_get_activation_steepness(resource $ann, int $layer, int $neuron): float
```php

Obtiene la pendiente de activación para la neurona número `neuron` en la capa número `layer`, contando la capa de entrada como capa 0.

No es posible obtener la pendiente de activación para neuronas de la capa de entrada.

La pendiente de una función de activación dice algo sobre cómo de rápido va la función de activación del mínimo al máximo. Un valor alto para la función de activación proporcionará un entrenamiento más agresivo.

Cuando se entrenan redes neuronales donde los valores de salida deberían estar en los extremos (normalmente 0 y 1, dependiendo de la función de activación), se puede emplear una función de activación (p.ej. 1.0).

La pendiente de activación predeterminada es 0.5.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`layer`  
El número de capa

`neuron`  
El número de neurona

## Valores devueltos

La pendiente de activación para la neurona o -1 si la neurona no está definida en la red neuronal, o `false` en caso de error.

## Véase también

`fann_set_activation_function`, `fann_set_activation_steepness_layer`, `fann_set_activation_steepness_hidden`, `fann_set_activation_steepness_output`, `fann_set_activation_steepness`
