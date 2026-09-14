---
title: fann_get_bit_fail_limit
description: Devuelve el límite de fallo de bit empleado durante un entrenamiento
source_url: https://www.php.net/manual/es/function.fann-get-bit-fail-limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-bit-fail-limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21120
---

fann_get_bit_fail_limit

Devuelve el límite de fallo de bit empleado durante un entrenamiento

## Descripción

```php
fann_get_bit_fail_limit(resource $ann): float
```php

Devuelve el límite de fallo de bit empleado durante un entrenamiento.

El límite de fallo de bit se emplea durante un entrenamiento donde la [función de parada](#constants.fann-stopfunc) esté establecida a `FANN_STOPFUNC_BIT`.

El límite es la diferencia máxima aceptada entre la salida provista y la salida real durante un entrenamiento. Cada salida que diverja más que este límite se cuenta como un bit de error. Esta diferencia se dividide entre dos al tratar con funciones de activación simétrica, por lo que las funciones de activación simétrica y no simétrica pueden utilizar el mismo límite.

El límite de fallo de bit es 0.35.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El límite de fallo de bit, o `false` en caso de error.

## Véase también

`fann_set_bit_fail_limit`
