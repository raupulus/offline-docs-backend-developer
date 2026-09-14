---
title: fann_get_rprop_delta_min
description: Devuelve el tamaño de paso mínimo
source_url: https://www.php.net/manual/es/function.fann-get-rprop-delta-min.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-rprop-delta-min.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21460
---

fann_get_rprop_delta_min

Devuelve el tamaño de paso mínimo

## Descripción

```php
fann_get_rprop_delta_min(resource $ann): float
```php

El tamaño de paso mínimo es un número positivo pequeño que determina lo pequeño que podría ser el tamaño de paso mínimo.

El valor predeterminado de delta mínimo es 0.0.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El tamaño de paso mínimo, o `false` en caso de error.

## Véase también

`fann_set_rprop_delta_min`
