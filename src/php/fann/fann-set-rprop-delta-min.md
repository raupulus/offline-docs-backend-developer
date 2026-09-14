---
title: fann_set_rprop_delta_min
description: Establece el tamaño de paso mínimo
source_url: https://www.php.net/manual/es/function.fann-set-rprop-delta-min.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-rprop-delta-min.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22100
---

fann_set_rprop_delta_min

Establece el tamaño de paso mínimo

## Descripción

```php
fann_set_rprop_delta_min(resource $ann, float $rprop_delta_min): bool
```php

El tamaño de paso mínimo es un número positivo pequeño que determina lo pequeño que podría ser el tamaño de paso mínimo.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`rprop_delta_min`  
El tamaño de paso mínimo.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_rprop_delta_min`
