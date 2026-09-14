---
title: fann_get_cascade_activation_steepnesses
description: Devuelve las pendientes de activación en cascada
source_url: https://www.php.net/manual/es/function.fann-get-cascade-activation-steepnesses.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-activation-steepnesses.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21170
---

fann_get_cascade_activation_steepnesses

Devuelve las pendientes de activación en cascada

## Descripción

```php
fann_get_cascade_activation_steepnesses(resource $ann): array
```php

El array de pendientes de activación en cascada es un array con las diferentes funciones de activación empleadas por las candidatas.

Véase `fann_get_cascade_num_candidates` para una descripción de las neuronas candidatas generadas por este array.

Las pendientes de activación predeterminadas son {0.25, 0.50, 0.75, 1.00}.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Las pendientes de activación en cascada, o `false` en caso de error.

## Véase también

`fann_get_cascade_activation_steepnesses_count`, `fann_set_cascade_activation_steepnesses`
