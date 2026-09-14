---
title: fann_get_cascade_activation_functions_count
description: Devuelve el número de funciones de activación en cascada
source_url: https://www.php.net/manual/es/function.fann-get-cascade-activation-functions-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-activation-functions-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21140
---

fann_get_cascade_activation_functions_count

Devuelve el número de funciones de activación en cascada

## Descripción

```php
fann_get_cascade_activation_functions_count(resource $ann): int
```php

El número de funciones de activación del array `fann_get_cascade_activation_functions`.

El número predeterminado de funciones de activación es 6.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número de funciones de activación en cascada, o `false` en caso de error.

## Véase también

`fann_get_cascade_activation_functions`, `fann_set_cascade_activation_functions`
