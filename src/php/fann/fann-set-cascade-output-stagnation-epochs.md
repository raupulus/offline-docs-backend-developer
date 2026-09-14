---
title: fann_set_cascade_output_stagnation_epochs
description: Establece el número de épocas de estancamiento de salida en cascada
source_url: https://www.php.net/manual/es/function.fann-set-cascade-output-stagnation-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-output-stagnation-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21990
---

fann_set_cascade_output_stagnation_epochs

Establece el número de épocas de estancamiento de salida en cascada

## Descripción

```php
fann_set_cascade_output_stagnation_epochs(resource $ann, int $cascade_output_stagnation_epochs): bool
```php

Establece el número de épocas de estancamiento de salida en cascada.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_output_stagnation_epochs`  
El número de épocas de estancamiento de salida en cascada.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_output_stagnation_epochs`
