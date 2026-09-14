---
title: fann_set_activation_steepness
description: Establece la pendiente de activación el número de neurona y capa proporcionados
source_url: https://www.php.net/manual/es/function.fann-set-activation-steepness.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-steepness.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 9ee27f088
order: 21850
---

fann_set_activation_steepness

Establece la pendiente de activación el número de neurona y capa proporcionados

## Descripción

```php
fann_set_activation_steepness(resource $ann, float $activation_steepness, int $layer, int $neuron): bool
```php

Establece la pendiente de activación en la neurona número `neuron` de la capa número `layer`, contando la capa de entrada como capa 0.

No es posible establecer una pendiente de activación en la capa de entrada.

La pendiente de una función de activación dice algo sobre cómo de rápido va la función de activación del mínimo al máximo. Un valor alto para la función de activación proporcionará un entrenamiento más agresivo.

Cuando se entrenan redes neuronales donde los valores de salida deberían estar en los extremos (normalmente 0 y 1, dependiendo de la función de activación), se puede emplear una función de activación (p.ej. 1.0).

La pendiente de activación predeterminada es 0.5.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_steepness`  
La pendiente de activación.

`layer`  
El número de capa.

`neuron`  
El número de neurona.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_steepness_layer`, `fann_set_activation_steepness_hidden`, `fann_set_activation_steepness_output`, `fann_get_activation_steepness`, `fann_set_activation_function`
