---
title: fann_get_rprop_delta_max
description: Devuelve el tamaño de paso máximo
source_url: https://www.php.net/manual/es/function.fann-get-rprop-delta-max.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-rprop-delta-max.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21450
---

fann_get_rprop_delta_max

Devuelve el tamaño de paso máximo

## Descripción

```php
fann_get_rprop_delta_max(resource $ann): float
```php

El tamaño de paso máximo es un número positivo que determina lo grande que podría ser el tamaño de paso máximo.

El valor predeterminado de delta máximo es 50.0.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El tamaño de paso máximo, o `false` en caso de error.

## Véase también

`fann_set_rprop_delta_max`, `fann_get_rprop_delta_min`
