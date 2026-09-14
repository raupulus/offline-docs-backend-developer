---
title: fann_reset_MSE
description: Reinicia el error cuadrático medio de la red
source_url: https://www.php.net/manual/es/function.fann-reset-mse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-reset-mse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21680
---

fann_reset_MSE

Reinicia el error cuadrático medio de la red

## Descripción

```php
fann_reset_MSE(string $ann): bool
```php

Reinicia el error cuadrático medio de la red.

Esta función también reinicia el número de bit que fallan.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_MSE`, `fann_get_bit_fail`, `fann_get_bit_fail_limit`
