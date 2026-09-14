---
title: fann_set_sarprop_step_error_threshold_factor
description: Establece el factor de umbral del error de paso de sarprop
source_url: https://www.php.net/manual/es/function.fann-set-sarprop-step-error-threshold-factor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-sarprop-step-error-threshold-factor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 242efce0d
order: 22140
---

fann_set_sarprop_step_error_threshold_factor

Establece el factor de umbral del error de paso de sarprop

## Descripción

```php
fann_set_sarprop_step_error_threshold_factor(resource $ann, float $sarprop_step_error_threshold_factor): bool
```php

Establece el factor de umbral del error de paso de sarprop.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`sarprop_step_error_threshold_factor`  
El factor de umbral del error de paso de sarprop.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_get_sarprop_step_error_threshold_factor`
