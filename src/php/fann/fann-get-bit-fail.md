---
title: fann_get_bit_fail
description: El número de bit fallidos
source_url: https://www.php.net/manual/es/function.fann-get-bit-fail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-bit-fail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21130
---

fann_get_bit_fail

El número de bit fallidos

## Descripción

```php
fann_get_bit_fail(resource $ann): int
```php

El número de bit fallidos; es el número de neuronas de salida que difieren más del límte de fallo de bit (véanse `fann_get_bit_fail_limit` y `fann_set_bit_fail_limit`). Los bit se cuentan en todos los datos de entrenamiento, por lo que este número puede ser mayor que el número de datos de entrenamiento.

Este valor es reiniciado por `fann_reset_MSE` y actualizado por las mismas funciones que también actualizan el valor del ECM (p.ej., `fann_test_data` y `fann_train_epoch`)

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número de bit fallidos, o `false` en caso de error.

## Véase también

`fann_get_MSE`, `fann_reset_MSE`, `fann_test_data`, `fann_train_epoch`, `fann_get_bit_fail_limit`, `fann_set_bit_fail_limit`
