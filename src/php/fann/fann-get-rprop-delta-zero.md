---
title: fann_get_rprop_delta_zero
description: Devuelve el tamaño de paso inicial
source_url: https://www.php.net/manual/es/function.fann-get-rprop-delta-zero.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-rprop-delta-zero.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21470
---

fann_get_rprop_delta_zero

Devuelve el tamaño de paso inicial

## Descripción

```php
fann_get_rprop_delta_zero(resource $ann): int
```php

El tamaño de paso inicial es un número positivo que determina el tamaño de paso inicial.

El valor predeterminado de delta cero es 0.1.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El tamaño de paso inicial, o `false` en caso de error.

## Véase también

`fann_set_rprop_delta_zero`, `fann_get_rprop_delta_min`, `fann_get_rprop_delta_max`
