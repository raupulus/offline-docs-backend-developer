---
title: fann_set_cascade_activation_steepnesses
description: Establece el array de pendientes de activación de candidatas en cascada
source_url: https://www.php.net/manual/es/function.fann-set-cascade-activation-steepnesses.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-activation-steepnesses.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21890
---

fann_set_cascade_activation_steepnesses

Establece el array de pendientes de activación de candidatas en cascada

## Descripción

```php
fann_set_cascade_activation_steepnesses(resource $ann, array $cascade_activation_steepnesses_count): bool
```php

Establece el array de pendientes de activación de candidatas en cascada.

Véase `fann_get_cascade_num_candidates` para una descripción de las neuronas candidatas generadas por este array.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_activation_steepnesses_count`  
El array de pendientes de activación de candidatas en cascada.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_activation_steepnesses`, `fann_get_cascade_activation_steepnesses_count`
