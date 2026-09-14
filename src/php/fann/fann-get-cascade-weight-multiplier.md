---
title: fann_get_cascade_weight_multiplier
description: Devuelve el multiplicador de peso
source_url: https://www.php.net/manual/es/function.fann-get-cascade-weight-multiplier.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-weight-multiplier.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21290
---

fann_get_cascade_weight_multiplier

Devuelve el multiplicador de peso

## Descripción

```php
fann_get_cascade_weight_multiplier(resource $ann): float
```php

El multiplicador de peso es un parámetro que se emplea para multiplicar los pesos de la neurona candidata antes de añadir la neurona a la red neuronal. Este parámetro está normalmente entre 0 y 1, y se emplea para hacer el entrenamiento un poco menos agresivo.

El multiplicador de peso predeterminado es 0.4.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El multiplicador de peso, o `false` en caso de error.

## Véase también

`fann_set_cascade_weight_multiplier`
