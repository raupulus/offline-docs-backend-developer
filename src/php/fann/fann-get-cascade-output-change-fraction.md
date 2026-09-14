---
title: fann_get_cascade_output_change_fraction
description: Devuelve la fracción de cambio de salida en cascada
source_url: https://www.php.net/manual/es/function.fann-get-cascade-output-change-fraction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-output-change-fraction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 21270
---

fann_get_cascade_output_change_fraction

Devuelve la fracción de cambio de salida en cascada

## Descripción

```php
fann_get_cascade_output_change_fraction(resource $ann): float
```php

La fracción de cambio de salida en cascada es un número entre 0 y 1 que determina lo grande que debería ser el cambio del valor de una fracción de `fann_get_MSE` en `fann_get_cascade_output_stagnation_epochs` durante el entrenamiento de las conexiones de salida, para que el entrenamiento no se estanque. Si el entrenamiento se estanca, el entrenamiento de las conexiones de salida finalizará y se prepararán nuevas candidatas.

Esto significa que si el ECM no cambia por una fracción de `fann_get_cascade_output_change_fraction` durante un período de `fann_get_cascade_output_stagnation_epochs`, el entrenamiento de las conexiones de salida se para delbido a que el entrenamiento ha estancado.

Si la fracción de cambio de salida en cascada es baja, las conexiones de salida serán entrenadas más, y si la fracción es alta, serán entrenadas menos.

La fracción de cambio de salida en cascada predeterminada es 0.01, que es equivalente a un cambio del 1% en el ECM.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

La fracción de cambio de salida en cascada, o `false` en caso de error.

## Véase también

`fann_set_cascade_output_change_fraction`, `fann_get_MSE`, `fann_get_cascade_output_stagnation_epochs`
