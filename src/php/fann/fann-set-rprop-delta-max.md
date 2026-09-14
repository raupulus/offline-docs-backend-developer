---
title: fann_set_rprop_delta_max
description: Establece el tamaño de paso máximo
source_url: https://www.php.net/manual/es/function.fann-set-rprop-delta-max.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-rprop-delta-max.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22090
---

fann_set_rprop_delta_max

Establece el tamaño de paso máximo

## Descripción

```php
fann_set_rprop_delta_max(resource $ann, float $rprop_delta_max): bool
```php

El tamaño de paso máximo es un número positivo que determina lo grande que podría ser el tamaño de paso máximo.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`rprop_delta_max`  
El tamaño de paso máximo.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_rprop_delta_max`, `fann_get_rprop_delta_min`
