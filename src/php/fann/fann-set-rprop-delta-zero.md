---
title: fann_set_rprop_delta_zero
description: Establece el tamaño de paso inicial
source_url: https://www.php.net/manual/es/function.fann-set-rprop-delta-zero.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-rprop-delta-zero.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22110
---

fann_set_rprop_delta_zero

Establece el tamaño de paso inicial

## Descripción

```php
fann_set_rprop_delta_zero(resource $ann, float $rprop_delta_zero): bool
```php

El tamaño de paso inicial es un número positivo que determina el tamaño de paso inicial.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`rprop_delta_zero`  
El tamaño de paso inicial.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_rprop_delta_zero`, `fann_get_rprop_delta_min`, `fann_get_rprop_delta_max`
