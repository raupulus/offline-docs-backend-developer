---
title: fann_get_sarprop_step_error_threshold_factor
description: Devuelve el factor de umbral del error de paso de sarprop
source_url: https://www.php.net/manual/es/function.fann-get-sarprop-step-error-threshold-factor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-sarprop-step-error-threshold-factor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21500
---

fann_get_sarprop_step_error_threshold_factor

Devuelve el factor de umbral del error de paso de sarprop

## Descripción

```php
fann_get_sarprop_step_error_threshold_factor(resource $ann): float
```php

Devuelve el factor de umbral del error de paso de sarprop.

El factor predeterminado es 0.1.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El factor de umbral del error de paso de sarprop, o `false` en caso de error.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_set_sarprop_step_error_threshold_factor`
